"""
Cobalt Agent - Finance Tool
Provides access to market data via Yahoo Finance.
"""

import yfinance as yf
from loguru import logger
from pydantic import BaseModel

class FinanceTool(BaseModel):
    """
    Tool for fetching real-time stock market data.
    """
    name: str = "finance"
    description: str = "Get stock price, volume, and company info. Input should be a ticker symbol (e.g., 'AAPL', 'NVDA')."

    def run(self, ticker: str) -> str:
        """
        Fetch stock data for a given ticker.
        """
        try:
            ticker = ticker.upper().strip()
            logger.info(f"Fetching market data for: {ticker}")
            
            stock = yf.Ticker(ticker)
            
            # 1. Fetch Price Data safely
            # 'fast_info' is usually reliable for price
            try:
                price = stock.fast_info.last_price
                prev_close = stock.fast_info.previous_close
                volume = stock.fast_info.last_volume
            except:
                # Fallback to .info if fast_info fails
                price = stock.info.get('currentPrice') or stock.info.get('regularMarketPrice', 0.0)
                prev_close = stock.info.get('previousClose', 0.0)
                volume = stock.info.get('volume', 0)

            # 2. Calculate Change
            if price and prev_close:
                change_pct = ((price - prev_close) / prev_close) * 100
            else:
                change_pct = 0.0

            # 3. Get Info (safely)
            info = stock.info
            mkt_cap = info.get('marketCap')
            high_52 = info.get('fiftyTwoWeekHigh')
            low_52 = info.get('fiftyTwoWeekLow')
            
            # 4. Helper to format numbers safely (Avoids the "Cannot specify ',' with 's'" error)
            def safe_fmt(val, is_currency=False):
                if isinstance(val, (int, float)):
                    if is_currency:
                        return f"${val:,.2f}"
                    return f"{val:,}"
                return "N/A"

            # Construct Report
            report = (
                f"### Market Data: {ticker}\n"
                f"- **Price:** {safe_fmt(price, True)}\n"
                f"- **Change:** {change_pct:+.2f}%\n"
                f"- **Volume:** {safe_fmt(volume)}\n"
                f"- **Market Cap:** {safe_fmt(mkt_cap)}\n"
                f"- **52w High:** {safe_fmt(high_52, True)}\n"
                f"- **52w Low:** {safe_fmt(low_52, True)}\n"
                f"- **Sector:** {info.get('sector', 'Unknown')}\n"
                f"- **Summary:** {info.get('longBusinessSummary', 'No summary available.')[:200]}..."
            )
            return report

        except Exception as e:
            logger.error(f"Finance Tool Error: {e}")
            return f"Error fetching data for {ticker}: {str(e)}"