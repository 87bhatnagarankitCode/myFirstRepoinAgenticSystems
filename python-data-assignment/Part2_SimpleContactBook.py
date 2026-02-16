
import os

os.system('cls')

contactDictn = {}

def createContacsDictn(UserInput):
    if not UserInput == "" :
        Name, Number = UserInput.split("|",1)
        Name, Number = Name.strip(), Number.strip()
        if Number.isdigit():
            contactDictn[Name] = Number
        else:
            print("Phone Number is not numeric. Please re-enter conatct name with correct number")
    return contactDictn


def display(args):
    if args == "TotalRecs":
        print("Dictionary is :", contactDictn)
    else:
        try:
             if contactDictn[args]:
                  print("Contact is FOUND")
             else:
                  print("Contact is  NOT FOUND")
        except KeyError:
                  print("Contact is  NOT FOUND. Key doesnt exist")


def InputFromUser():
    print(" *** In case you don't want to add Contacts, Press 'q'/'Q' ***") 
    print("\n ### Enter Contact Name & Phone Number separated with pipe e.g. Alice|9123456790 ")
    counter = 0
    while True:
        if len(contactDictn) == 3:
            print("****You have added 3 contact details. You can proceed or stop.*****")

        UserInput = input(" > Please provide your input or Press 'q'/'Q' to stop adding contacts : ")
        if (UserInput.lower() in ('q')):
            break
        elif ("|" not in UserInput ) or  (UserInput == ""):
            print("Invalid input given. Kindly correct")
        else:
            createContacsDictn(UserInput)
            counter += 1

def InputUserTosearch():
    UserInput = input(" >> Please enter userName to search in the dictionary : ").strip()
    if UserInput =="":
        print("Invalid username to search")
    else:
        print("Please wait ..searching......")
        display(UserInput)

def main():
    InputFromUser()
    display("TotalRecs")  
    InputUserTosearch()

main()