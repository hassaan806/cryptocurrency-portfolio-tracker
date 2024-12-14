# Cryptocurrency Portfolio Tracker

The Cryptocurrency Portfolio Tracker is a Python application that allows users to manage and track their cryptocurrency holdings. Users can add cryptocurrencies to their portfolio, view their portfolio, and check the total value of their portfolio based on live cryptocurrency prices from Binance.

## Features

1. **Add Cryptocurrency**: Add cryptocurrency holdings to your portfolio by specifying the symbol and amount.
2. **View Portfolio**: View the list of cryptocurrencies in your portfolio along with their respective amounts.
3. **Check Portfolio Value**: Fetch live cryptocurrency prices from Binance and calculate the total value of your portfolio.
4. **User-Friendly Menu**: Simple menu-based navigation to perform actions.

## Prerequisites

- Python 3.x installed on your system.
- An active internet connection (for fetching live cryptocurrency prices).
- The `requests` library installed. You can install it via pip if not already installed:

```bash
pip install requests
```

## How to Run the Program

1. Clone or download this repository to your local system.
2. Navigate to the directory containing the script.
3. Run the script using Python:

```bash
python tracker.py
```

4. Follow the on-screen instructions to interact with the program.

## Usage

### Menu Options

1. **Add Cryptocurrency**: Enter the cryptocurrency symbol (e.g., BTC for Bitcoin) and the amount you own. The program validates the symbol using Binance's API.
2. **View Portfolio**: Displays the list of all cryptocurrencies in your portfolio along with their respective amounts.
3. **Check Portfolio Value**: Fetches the latest prices for each cryptocurrency in your portfolio from Binance and calculates the total portfolio value.
4. **Exit**: Exit the application.

### Example Run

#### Adding Cryptocurrency
```
Enter the cryptocurrency symbol (e.g., BTC for Bitcoin): BTC
How many BTC do you own? 0.5
Added 0.5 BTC to your portfolio.
```

#### Viewing Portfolio
```
Your Portfolio:
BTC: 0.5 units
```

#### Checking Portfolio Value
```
Fetching latest cryptocurrency prices...
BTC: 0.5 units @ $30000.00 each = $15000.00

Total Portfolio Value: $15000.00
```

## Code Explanation

### Main Modules

1. **`main()`**: Handles the main menu logic and user input.
2. **`add_crypto()`**: Adds a new cryptocurrency to the portfolio or updates the amount if it already exists.
3. **`view_portfolio()`**: Displays the contents of the portfolio.
4. **`check_portfolio_value()`**: Fetches live prices and calculates the portfolio's total value.
5. **`get_crypto_price(symbol)`**: Fetches the live price of a cryptocurrency from Binance's API.
6. **`is_valid_symbol(symbol)`**: Validates a cryptocurrency symbol by checking Binance's exchange info API.

### External API

The program uses Binance's public API to:
- Fetch live cryptocurrency prices.
- Validate cryptocurrency symbols.

### Error Handling

- Invalid inputs (e.g., non-numeric amounts) are handled gracefully.
- API connection issues or invalid symbols display appropriate error messages.

## Limitations

- The program only supports cryptocurrencies traded against USDT on Binance.
- Internet connection is required to fetch live prices and validate symbols.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it.

---

Feel free to contact the developer for any questions or suggestions!
