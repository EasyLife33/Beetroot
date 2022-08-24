stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
whole_stock = []
whole_prices = []
smth = 0

for i in stock:
    whole_stock.append(stock[i])
for i in prices:
    whole_prices.append(prices[i])
for i in range(len(whole_prices)):
    smth += whole_stock[i] * whole_prices[i]
print(f"price of fruits: {int(smth)}$")
