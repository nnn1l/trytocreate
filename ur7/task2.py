#Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.

#The code has to return the dictionary with the sums of the prices by the goods types.

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

all_fruits_cost = {}
for name, amount in stock.items():
    for price in prices.values():
        all_fruits_cost[name] = amount * price
print(all_fruits_cost)

