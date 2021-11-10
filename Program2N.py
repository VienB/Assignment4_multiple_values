def FirstGroup():
    ApplesFunc = int(input ("Enter the quantity of apples that you want to buy: "))
    OrangesFunc = int(input ("Enter the quantity of oranges that you want to buy: "))
    return ApplesFunc, OrangesFunc

def SecondGroup(Apples, Oranges):
    PriceApplesFunc = Apples * 20
    PriceOrangesFunc = Oranges * 25
    return  PriceApplesFunc, PriceOrangesFunc

def FinalOutput(PriceOfApple1, PriceOfOrange1):
    print (f'The total amount is {PriceOfApple1 + PriceOfOrange1}')

Apples, Oranges = FirstGroup()
PriceOfApple, PriceOfOrange = SecondGroup(Apples, Oranges)
FinalOutput (PriceOfApple, PriceOfOrange)