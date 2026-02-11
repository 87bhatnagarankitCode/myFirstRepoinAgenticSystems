
import os

os.system('cls')
def InputNumber():
    while True:
        try:
            Number = int(input("\n Please enter a number to check if its an Even or Odd = "))
            return Number
        except ValueError:
             print("Enter Valid number")

def EvenOddchecker():
    if InputNumber() % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"
    
def printResponse():
    print(f"\n{EvenOddchecker()}")
    
printResponse()

