from cs50 import get_float

quarter = 25
dime = 10
nickel = 5
penny = 1
coins = 0

while True:
    change = get_float("How much change do I owe you? ")
    if change > 0:
        break
    
change = round(int(change * 100))    
   
while change > 0:
    while change >= quarter:
        coins += 1
        change -= quarter
    while change >= dime:
        coins += 1
        change -= dime
    while change >= nickel:
        coins += 1
        change -= nickel
    while change >= penny:
        change -= penny
        coins += 1
        
print(coins)