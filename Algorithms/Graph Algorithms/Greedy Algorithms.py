# Greedy Algorithm example: Coin changing problem

def coin_change(coins, amount):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change

coins = [1, 2, 5, 10, 20, 50]
amount = 63
print(coin_change(coins, amount))  # [50, 10, 2, 1]