import requests

def main():
    print("Welcome to the Cryptocurrency Portfolio Tracker!")
    portfolio = {}
    
    while True:
        print("\nMenu:")
        print("1. Add Cryptocurrency")
        print("2. View Portfolio")
        print("3. Check Portfolio Value")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_crypto(portfolio)
        elif choice == "2":
            view_portfolio(portfolio)
        elif choice == "3":
            check_portfolio_value(portfolio)
        elif choice == "4":
            print("Exiting. Thank you for using the tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_crypto(portfolio):
    while True:
        symbol = input("Enter the cryptocurrency symbol (e.g., BTC for Bitcoin): ").upper()
        if is_valid_symbol(symbol):
            try:
                amount = float(input(f"How many {symbol} do you own? "))
                if symbol in portfolio:
                    portfolio[symbol] += amount
                else:
                    portfolio[symbol] = amount
                print(f"Added {amount} {symbol} to your portfolio.")
                break
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        else:
            print(f"'{symbol}' is not a valid cryptocurrency symbol. Please try again.")

def view_portfolio(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        print("\nYour Portfolio:")
        for symbol, amount in portfolio.items():
            print(f"{symbol}: {amount} units")

def check_portfolio_value(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\nFetching latest cryptocurrency prices...")
    total_value = 0.0

    for symbol, amount in portfolio.items():
        price = get_crypto_price(symbol)
        if price is not None:
            value = amount * price
            print(f"{symbol}: {amount} units @ ${price:.2f} each = ${value:.2f}")
            total_value += value
        else:
            print(f"Could not fetch price for {symbol}.")

    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

def get_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return float(data["price"])
    return None

def is_valid_symbol(symbol):
    url = "https://api.binance.com/api/v3/exchangeInfo"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            symbols = [s['symbol'] for s in data['symbols']]
            return f"{symbol}USDT" in symbols
    except Exception as e:
        print(f"Error validating symbol: {e}")
    return False


if __name__ == "__main__":
    main()
