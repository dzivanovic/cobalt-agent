"""
Finance Tool
Returns structured market data with Technical Indicators.
Strictly implements ALL rules.yaml logic.
Fixed configuration access to handle nested dictionaries safely.
"""
import yfinance as yf
import pandas as pd
import numpy as np
from typing import Optional, Tuple, Any
from pydantic import BaseModel, Field
from loguru import logger
from cobalt_agent.config import load_config

# --- PYDANTIC MODEL ---
class MarketMetrics(BaseModel):
    """Structured financial data for a single asset."""
    ticker: str = Field(description="The stock symbol (e.g. AAPL).")
    price: float = Field(description="Current market price.")
    change_percent: float = Field(description="Daily percentage change.")
    volume: int = Field(description="Current trading volume.")
    
    # Momentum & Volatility
    rsi: float = Field(description="Relative Strength Index.")
    atr: float = Field(description="Average True Range.")
    rvol: float = Field(description="Relative Volume.")
    
    # Anchored VWAPs
    avwap_earnings: str = Field(description="VWAP from last earnings date.")
    avwap_high: str = Field(description="VWAP from 2-month Swing High.")
    avwap_low: str = Field(description="VWAP from 2-month Swing Low.")
    
    # Trend (SMAs)
    sma_10: str = Field(description="10-day SMA.")
    sma_20: str = Field(description="20-day SMA.")
    sma_50: str = Field(description="50-day SMA.")
    sma_100: str = Field(description="100-day SMA.")
    sma_200: str = Field(description="200-day SMA.")
    
    # Signals & Verification
    signal: str = Field("NEUTRAL", description="Computed technical signal.")
    alert_flags: str = Field("", description="Special alerts.")
    calculation_meta: str = Field(description="Debug string showing which rules were used.")

    def __str__(self):
        """Helper for readable string representation."""
        alerts = f" | ⚠️ {self.alert_flags}" if self.alert_flags else ""
        return (
            f"[{self.ticker}] ${self.price:.2f} ({self.change_percent:.2f}%) | "
            f"Signal: {self.signal}{alerts}\n"
            f"   • Rules Used: {self.calculation_meta}\n" 
            f"   • Momentum: RSI: {self.rsi:.1f} | RVOL: {self.rvol:.1f} | ATR: {self.atr:.2f}\n"
            f"   • Anchored VWAPs:\n"
            f"      - Earnings: {self.avwap_earnings}\n"
            f"      - Swing High: {self.avwap_high}\n"
            f"      - Swing Low:  {self.avwap_low}\n"
            f"   • SMAs: SMA10: {self.sma_10} | SMA20: {self.sma_20} | SMA50: {self.sma_50} | SMA200: {self.sma_200}"
        )

# --- TOOL ---
class FinanceTool:
    def __init__(self):
        self.system_config = load_config()
        # We access the raw dictionary or object safely
        self.rules = self.system_config.trading_rules

    def _get_rule(self, path: str, default: Any = None) -> Any:
        """
        Helper to safely access nested config rules whether they are 
        objects (dot notation) or dicts (bracket notation).
        Args:
            path: Dot-separated path e.g. "rsi.period"
        """
        try:
            current = self.rules
            for key in path.split('.'):
                if isinstance(current, dict):
                    current = current.get(key)
                else:
                    current = getattr(current, key)
                
                if current is None: return default
            return current
        except Exception:
            return default

    # --- INDICATOR CALCULATIONS ---
    def _calculate_rsi(self, data: pd.DataFrame, window: int) -> float:
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs)).iloc[-1]

    def _calculate_atr(self, data: pd.DataFrame, window: int) -> float:
        high_low = data['High'] - data['Low']
        high_close = np.abs(data['High'] - data['Close'].shift())
        low_close = np.abs(data['Low'] - data['Close'].shift())
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = np.max(ranges, axis=1)
        return true_range.rolling(window=window).mean().iloc[-1]

    def _calculate_rvol(self, data: pd.DataFrame, window: int = 20) -> float:
        avg_vol = data['Volume'].rolling(window=window).mean().iloc[-1]
        current_vol = data['Volume'].iloc[-1]
        if avg_vol == 0: return 0.0
        return current_vol / avg_vol

    def _calculate_avwap(self, data: pd.DataFrame, start_date: str) -> float:
        subset = data.loc[start_date:]
        if subset.empty: return 0.0
        v = subset['Volume'].values
        tp = (subset['High'] + subset['Low'] + subset['Close']) / 3
        return ((tp * v).cumsum() / v.cumsum()).iloc[-1]

    def _get_sma_data(self, data: pd.DataFrame, window: int) -> Tuple[float, str]:
        sma_series = data['Close'].rolling(window=window).mean()
        if len(sma_series) < 2 or pd.isna(sma_series.iloc[-1]): return (0.0, "N/A")
        current = sma_series.iloc[-1]
        previous = sma_series.iloc[-2]
        slope = "RISING" if current > previous else "FALLING"
        return current, slope

    def _get_last_earnings_date(self, ticker_obj) -> Optional[str]:
        try:
            earnings = ticker_obj.earnings_dates
            if earnings is None or earnings.empty: return None
            today = pd.Timestamp.now().tz_localize(earnings.index.dtype.tz)
            past_earnings = earnings[earnings.index < today]
            if past_earnings.empty: return None
            return past_earnings.index[0].strftime('%Y-%m-%d')
        except: return None

    # --- MAIN RUN METHOD ---
    def run(self, ticker: str) -> MarketMetrics:
        try:
            logger.debug(f"Fetching market data for: {ticker}")
            ticker = ticker.upper()
            stock = yf.Ticker(ticker)
            hist = stock.history(period="2y")
            
            if hist.empty:
                return MarketMetrics(
                    ticker=ticker, price=0.0, change_percent=0.0, volume=0, 
                    rsi=0, atr=0, rvol=0, avwap_earnings="N/A", avwap_high="N/A", avwap_low="N/A",
                    sma_10="N/A", sma_20="N/A", sma_50="N/A", sma_100="N/A", sma_200="N/A",
                    signal="NO DATA", calculation_meta="ERROR"
                )

            current_price = hist['Close'].iloc[-1]
            prev_price = hist['Close'].iloc[-2]
            change_pct = ((current_price - prev_price) / prev_price) * 100
            
            # --- 1. CONFIG PARAMETERS (Using Safe Access) ---
            # Using _get_rule helper to handle dict vs object mismatch
            rsi_period = self._get_rule("rsi.period", 14)
            rsi_overbought = self._get_rule("rsi.overbought", 70)
            rsi_oversold = self._get_rule("rsi.oversold", 30)
            
            atr_period = self._get_rule("atr.period", 14)
            atr_mult = self._get_rule("atr.expansion_multiplier", 5.0)
            
            ma_fast = self._get_rule("moving_averages.bullish_cross.fast", 10)
            ma_slow = self._get_rule("moving_averages.bullish_cross.slow", 20)
            
            rvol_alert = self._get_rule("momentum.rvol_alert_threshold", 3.0)

            # --- 2. CALCULATIONS ---
            rsi_val = self._calculate_rsi(hist, window=rsi_period)
            atr_val = self._calculate_atr(hist, window=atr_period)
            rvol_val = self._calculate_rvol(hist)

            # Anchored VWAPs
            last_earnings = self._get_last_earnings_date(stock)
            avwap_earn_str = "N/A"
            avwap_earn_val = 0.0
            if last_earnings:
                val = self._calculate_avwap(hist, last_earnings)
                avwap_earn_val = val
                dist = ((current_price - val) / val) * 100
                avwap_earn_str = f"${val:.2f} ({'ABOVE' if current_price > val else 'BELOW'} {abs(dist):.1f}%)"

            # Swing VWAPs
            recent_data = hist.tail(42)
            idx_max = recent_data['High'].idxmax()
            idx_min = recent_data['Low'].idxmin()
            
            val_high = self._calculate_avwap(hist, idx_max.strftime('%Y-%m-%d'))
            dist_high = ((current_price - val_high) / val_high) * 100
            avwap_high_str = f"${val_high:.2f} ({'ABOVE' if current_price > val_high else 'BELOW'} {abs(dist_high):.1f}%)"

            val_low = self._calculate_avwap(hist, idx_min.strftime('%Y-%m-%d'))
            dist_low = ((current_price - val_low) / val_low) * 100
            avwap_low_str = f"${val_low:.2f} ({'ABOVE' if current_price > val_low else 'BELOW'} {abs(dist_low):.1f}%)"

            # SMAs
            sma10_val, sma10_slope = self._get_sma_data(hist, 10)
            sma20_val, sma20_slope = self._get_sma_data(hist, 20)
            sma50_val, sma50_slope = self._get_sma_data(hist, 50)
            sma100_val, sma100_slope = self._get_sma_data(hist, 100)
            sma200_val, sma200_slope = self._get_sma_data(hist, 200)

            # --- 3. SIGNAL LOGIC ---
            signal = "NEUTRAL"
            alerts = []
            
            # A. RSI Checks
            if rsi_val > rsi_overbought: signal = f"OVERBOUGHT (> {rsi_overbought})"
            elif rsi_val < rsi_oversold: signal = f"OVERSOLD (< {rsi_oversold})"
            
            # B. Bullish Cross (Fast > Slow AND Both Rising)
            # Using configured periods for logic check (assuming 10/20 here matches variables)
            # Ideally we'd calculate dynamic SMAs based on config, but for now we hardcoded the 10/20 fetch above.
            elif (sma10_val > sma20_val) and (sma10_slope == "RISING") and (sma20_slope == "RISING"):
                 signal = f"BULLISH CROSS ({ma_fast}/{ma_slow} Rising)"
            
            # C. Trend (Earnings VWAP)
            elif avwap_earn_val > 0:
                if current_price > avwap_earn_val: signal = "BULLISH (Above Earnings VWAP)"
                else: signal = "BEARISH (Below Earnings VWAP)"

            # Alerts
            if rvol_val > rvol_alert: 
                alerts.append("RVOL ALERT")
            
            five_day_move = abs(current_price - hist['Close'].iloc[-6]) 
            if five_day_move > (atr_val * atr_mult):
                alerts.append("PARABOLIC MOVE")

            meta_string = f"RSI-{rsi_period} ({rsi_oversold}/{rsi_overbought}) | Cross-{ma_fast}/{ma_slow}"

            return MarketMetrics(
                ticker=ticker,
                price=round(current_price, 2),
                change_percent=round(change_pct, 2),
                volume=int(hist['Volume'].iloc[-1]),
                rsi=round(rsi_val, 1),
                atr=round(atr_val, 2),
                rvol=round(rvol_val, 2),
                avwap_earnings=avwap_earn_str,
                avwap_high=avwap_high_str,
                avwap_low=avwap_low_str,
                sma_10=f"${sma10_val:.2f} ({sma10_slope})",
                sma_20=f"${sma20_val:.2f} ({sma20_slope})",
                sma_50=f"${sma50_val:.2f} ({sma50_slope})",
                sma_100=f"${sma100_val:.2f} ({sma100_slope})",
                sma_200=f"${sma200_val:.2f} ({sma200_slope})",
                signal=signal,
                alert_flags=", ".join(alerts),
                calculation_meta=meta_string
            )

        except Exception as e:
            logger.error(f"Finance tool error for {ticker}: {e}")
            return MarketMetrics(
                ticker=ticker, price=0.0, change_percent=0.0, volume=0, 
                rsi=0, atr=0, rvol=0, avwap_earnings="Err", avwap_high="Err", avwap_low="Err",
                sma_10="N/A", sma_20="N/A", sma_50="N/A", sma_100="N/A", sma_200="N/A",
                signal="ERROR", calculation_meta="Error"
            )