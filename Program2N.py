# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

print("Vien Angelo Bernales / BSCOE 1-1 \n")
#use a function and return multiple values
def AppleOrange():
    AppleF = int(input("How many apple you want to buy? "))
    OrangeF = int(input("How many orange you want to buy? "))
    return AppleF, OrangeF

def Calculate(Applef, Orangef):
    Aoutcome = AppleQ * 20
    Ooutcome = OrangeQ * 25
    return Aoutcome, Ooutcome

def DisplayQ(Apple1, Orange1):
    print(f"The total amount is {Apple1 + Orange1}.")


AppleQ, OrangeQ = AppleOrange()
APrice, Oprice = Calculate(AppleQ, OrangeQ)
DisplayQ(APrice, Oprice)
