# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

print("Vien Angelo Bernales / BSCOE 1-1 \n")

#use a function and return multiple values

def YourMoney():
    fee = int(input("how much money do you have? "))
    price = int(input("Enter the price of the apple: "))
    return fee, price

def getTotal(moneyQ, appleQ):
    TotalApples = int(moneyQ / appleQ)
    amount = int(moneyQ % appleQ)
    return TotalApples, amount

def getOutput(affordable, changeF):
    print(f"You can buy {affordable} apples and your change is {changeF} pesos.")

moneyF, apple = YourMoney()
Tamount, change = getTotal(moneyF, apple)
getOutput(Tamount, change)