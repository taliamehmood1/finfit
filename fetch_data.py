import yfinance as yf

# Step 1: Choose a stock symbol (example: Apple = AAPL)
ticker_symbol = "AAPL"

# Step 2: Download last 1 month of daily data
stock = yf.Ticker(ticker_symbol)
data = stock.history(period="1mo")

# Step 3: Show the top rows
print(data.head())
