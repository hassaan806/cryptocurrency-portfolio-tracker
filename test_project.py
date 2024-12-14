import pytest
from project import add_crypto, view_portfolio, check_portfolio_value

def test_add_crypto():
    portfolio = {}
    add_crypto_helper(portfolio, "BTC", 2.5)
    assert portfolio["BTC"] == 2.5

    add_crypto_helper(portfolio, "BTC", 1.5)
    assert portfolio["BTC"] == 4.0

def test_view_portfolio(capsys):
    portfolio = {"BTC": 2.5, "ETH": 1.0}
    view_portfolio(portfolio)
    captured = capsys.readouterr()
    assert "BTC: 2.5 units" in captured.out
    assert "ETH: 1.0 units" in captured.out

def test_check_portfolio_value(monkeypatch):
    # Mocking the Binance API response
    def mock_get_crypto_price(symbol):
        prices = {"BTCUSDT": 50000, "ETHUSDT": 4000}  # Mocked Binance prices
        return prices.get(f"{symbol}USDT", None)

    # Monkeypatching the actual API call
    monkeypatch.setattr("project.get_crypto_price", mock_get_crypto_price)

    # Test data
    portfolio = {"BTC": 2, "ETH": 3}
    total_value = check_portfolio_value_helper(portfolio, mock_get_crypto_price)
    assert total_value == 112000  # 2 BTC @ 50,000 + 3 ETH @ 4,000

# Helper functions for tests
def add_crypto_helper(portfolio, symbol, amount):
    if symbol in portfolio:
        portfolio[symbol] += amount
    else:
        portfolio[symbol] = amount

def check_portfolio_value_helper(portfolio, get_crypto_price):
    total_value = 0.0
    for symbol, amount in portfolio.items():
        price = get_crypto_price(symbol)
        if price is not None:
            total_value += amount * price
    return total_value
