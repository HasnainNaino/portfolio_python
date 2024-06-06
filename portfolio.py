import requests

# Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol):
        if symbol in self.portfolio:
            print(f"{symbol} is already in the portfolio.")
            return

        # Fetch stock data from Alpha Vantage API
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if 'Global Quote' in data:
            stock_data = data['Global Quote']
            self.portfolio[symbol] = {
                'price': float(stock_data['05. price']),
                'change': float(stock_data['09. change']),
            }
            print(f"{symbol} added to the portfolio.")
        else:
            print(f"Failed to fetch data for {symbol}.")

    def remove_stock(self, symbol):
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"{symbol} removed from the portfolio.")
        else:
            print(f"{symbol} is not in the portfolio.")

    def display_portfolio(self):
        print("Portfolio:")
        for symbol, data in self.portfolio.items():
            print(f"{symbol}: Price - {data['price']}, Change - {data['change']}")

if __name__ == "__main__":
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            portfolio.add_stock(symbol)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            portfolio.remove_stock(symbol)
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
