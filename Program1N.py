# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .
print("Vien Angelo Bernales / BSCOE 1-1 \n")

def getInfo():
    name = input("ENTER YOUR NAME: ")
    age = input("ENTER YOUR AGE: ")
    address = input("ENTER YOUR ADDRESS: ")
    return name, age, address

def display(name1, age1, add1):
    print(f"Hi, my name is {name1}. I am {age1} years old and I live in {add1} .")


nameQ, ageQ, addQ = getInfo()
display(nameQ, ageQ, addQ) 