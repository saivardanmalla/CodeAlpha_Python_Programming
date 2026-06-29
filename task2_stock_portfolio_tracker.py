stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 140
}

portfolio = {}
total = 0

count = int(input("How many stocks do you want to add? "))

for i in range(count):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print("Stock not available")

print("\nPortfolio Summary")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total += value
    print(stock, "Quantity:", quantity, "Value:", value)

print("Total Investment:", total)

with open("portfolio_result.txt", "w") as file:
    file.write(f"Total Investment: {total}")
