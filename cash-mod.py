from cs50 import get_float

coins = 0

# Request the change value from user and check for a positive number
while True:
    change = get_float("How much change do I owe you? ")
    if change > 0:
        break

# convert the change value in an integer
change = round(int(change * 100))

# calculate the quantity of coins
coins = change // 25
change %= 25

coins += change // 10
change %= 10

coins += change // 5
change %= 5

coins += change // 1

# print quantity of coins
print(coins)