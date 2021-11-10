# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

#use a function and return multiple values
def AppleOrange():
    AppleF = ("How many apple you want to buy? ")
    OrangeF = ("How many orange you want to buy? ")
    return AppleF, OrangeF

def Calculate():
    apple = 20
    orange = 25
    outcome = (apple)

AppleQ, OrangeQ = AppleOrange()
