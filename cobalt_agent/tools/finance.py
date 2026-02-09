"""
Cobalt Agent - Finance Tool
Institutional Grade: Anchored VWAP, SMAs, RSI, ATR Multiples.
Reads dynamic thresholds AND periods from rules.yaml.
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
from loguru import logger
from pydantic import BaseModel
from cobalt_agent.config import load_config

class FinanceTool(BaseModel):
    name: str = "finance"
    description: str = "Get stock price, Anchored VWAPs, RSI, ATR. Checks for Momentum Alerts."

    def run(self, ticker: str) -> str:
        try:
            ticker = ticker.upper().strip()
            logger.info(f"Fetching institutional data for: {ticker}")
            
            # --- LOAD DYNAMIC RULES ---
            config = load_config()
            rules = config.trading_rules
            
            # Fallback Defaults (if rules.yaml is missing)
            RVOL_ALERT = rules.momentum.rvol_alert_threshold if rules else 3.0
            
            # RSI Rules
            RSI_PERIOD = rules.rsi.period if rules else 14  # <--- DYNAMIC PERIOD
            RSI_OB = rules.rsi.overbought if rules else 80
            RSI_OS = rules.rsi.oversold if rules else 20
            
            # ATR Rules
            ATR_PERIOD = rules.atr.period if rules else 14
            ATR_PARABOLIC = rules.atr.expansion_multiplier if rules else 5.0
            
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1y")
            
            if hist.empty or len(hist) < 200:
                return f"Insufficient data for {ticker}."

            current_close = hist['Close'].iloc[-1]
            prev_close = hist['Close'].iloc[-2]
            current_vol = hist['Volume'].iloc[-1]
            
            # --- CALCULATIONS ---

            # 1. RVOL
            avg_vol = hist['Volume'].rolling(window=20).mean().iloc[-1]
            rvol = current_vol / avg_vol if avg_vol > 0 else 0.0

            # 2. RSI (Dynamic Period)
            delta = hist['Close'].diff()
            # Use RSI_PERIOD from config
            gain = (delta.where(delta > 0, 0)).rolling(window=RSI_PERIOD).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=RSI_PERIOD).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            current_rsi = rsi.iloc[-1]

            # 3. ATR (Dynamic Period)
            high_low = hist['High'] - hist['Low']
            high_close = np.abs(hist['High'] - hist['Close'].shift())
            low_close = np.abs(hist['Low'] - hist['Close'].shift())
            tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
            atr = tr.rolling(window=ATR_PERIOD).mean().iloc[-1]
            
            # 5-Day Move
            price_5d = hist['Close'].iloc[-6]
            move_5d = current_close - price_5d
            atr_multiple = abs(move_5d / atr)

            # --- ANCHORED VWAP (Standard) ---
            def calculate_avwap(df, anchor_idx):
                subset = df.loc[anchor_idx:]
                if subset.empty: return None
                cumulative_pv = (subset['Close'] * subset['Volume']).cumsum()
                cumulative_vol = subset['Volume'].cumsum()
                return (cumulative_pv / cumulative_vol).iloc[-1]

            # Anchor 1: Earnings
            avwap_earnings = None
            last_earnings_date = "Unknown"
            try:
                earnings = stock.earnings_dates
                if earnings is not None and not earnings.empty:
                    now_tz = pd.Timestamp.now().tz_localize(earnings.index.tz)
                    past_earnings = earnings.index[earnings.index < now_tz]
                    if not past_earnings.empty:
                        last_earn_dt = past_earnings[0]
                        idx_loc = hist.index.searchsorted(last_earn_dt)
                        if idx_loc < len(hist):
                            anchor_date = hist.index[idx_loc]
                            avwap_earnings = calculate_avwap(hist, anchor_date)
                            last_earnings_date = anchor_date.strftime('%Y-%m-%d')
            except Exception:
                pass

            # Anchor 2 & 3: High/Low
            high_idx = hist['High'].idxmax()
            avwap_high = calculate_avwap(hist, high_idx)
            low_idx = hist['Low'].idxmin()
            avwap_low = calculate_avwap(hist, low_idx)

            # --- ALERTS ---
            alerts = []
            if rvol > RVOL_ALERT:
                alerts.append(f"🚀 MOMENTUM ALERT: RVOL {rvol:.1f}x (> {RVOL_ALERT}x)")
            
            if current_rsi > RSI_OB:
                alerts.append(f"⚠️ OVERBOUGHT: RSI {current_rsi:.1f} (> {RSI_OB})")
            elif current_rsi < RSI_OS:
                alerts.append(f"🟢 OVERSOLD: RSI {current_rsi:.1f} (< {RSI_OS})")

            if atr_multiple > ATR_PARABOLIC:
                alerts.append(f"⚠️ PARABOLIC: Move is {atr_multiple:.1f}x ATR (> {ATR_PARABOLIC}x)")

            alert_section = ""
            if alerts:
                alert_section = "\n### 🚨 ACTIVE ALERTS\n" + "\n".join([f"- {a}" for a in alerts]) + "\n"

            # --- REPORT ---
            def fmt(val): return f"${val:.2f}" if val is not None else "N/A"

            report = (
                f"### Market Data: {ticker}\n"
                f"- **Price:** ${current_close:,.2f}\n"
                f"- **Change:** {((current_close - prev_close)/prev_close)*100:+.2f}%\n"
                f"- **RVOL:** {rvol:.2f}x\n"
                f"{alert_section}\n"
                f"### Technicals\n"
                f"- **RSI ({RSI_PERIOD}):** {current_rsi:.1f}\n"  # <--- THIS IS THE FIX. It tells LLM the period.
                f"- **ATR ({ATR_PERIOD}):** {atr:.2f}\n"
                f"- **ATR Multiple (5d):** {atr_multiple:.1f}x\n\n"
                f"### Anchored VWAP\n"
                f"- **Earnings:** {fmt(avwap_earnings)}\n"
                f"- **High:** {fmt(avwap_high)}\n"
                f"- **Low:** {fmt(avwap_low)}"
            )
            return report

        except Exception as e:
            logger.error(f"Finance Tool Error: {e}")
            return f"Error: {str(e)}"