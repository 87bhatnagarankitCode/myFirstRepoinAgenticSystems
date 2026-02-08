
def printnum(range_input):
    for i in range(range_input + 1):
        print(i)

def user_input():
    try:
        input_number = int(input("Please enter the range to print : "))
        printnum(input_number)
    except ValueError:
        print(" Incorrect value, enter valid number to print")    

user_input()
