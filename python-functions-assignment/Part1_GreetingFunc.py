import os ,sys

def Greeting(Username):
    return (f"Hello, {Username}!")

def inputName():
    while True:
        name= input(" Please enter user name : ")
        if name.strip() == "":
           print("\n !!!!!! Please enter correct name !!!!!!")
        else:
            return name
    

print(Greeting(inputName()))
