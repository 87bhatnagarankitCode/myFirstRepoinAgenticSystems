DataBase =[]

def getUserInput():
    inputName = input("Enter UserName :").strip()
    inputMarks =[]
    marksString = input("Enter Marks separated by pipe sign :").split("|")
    for mark in marksString:
        try:
            floatmark = float(mark.strip())
            if (floatmark > 100):
                print(f"Invalid mark  for the user {inputName}, Cant exceed more than 100. placing 0 for this subject ")
                floatmark = 0
            inputMarks.append(floatmark) 
        except ValueError:
            print(f"Marks list is invalid for userName {inputName}")
            inputMarks =[]
  
    inputRoles = {role.strip().lower()  for role in input("Enter roles separated by ';' sign : ").split(";")}

    UserDictionary =  {
                     "Name"    : inputName,
                     "Scores"  : inputMarks,
                     "Roles"   : inputRoles
                    }
    DataBase.append(UserDictionary)

def calculate_average(users):
    
    averages = {}
    for user in users:
        if user["Scores"]:  
            avg = sum(user["Scores"]) / len(user["Scores"])
        else:
            avg = 0
        averages[user["Name"]] = avg
    return averages

def hasAdminAccess(roles):
    return "admin" in roles



def main():
    while True:
        ch = input("Press q or Q to stop and any other key to continue : ").lower()
        if (ch == "q"):
            break
        else:
            getUserInput()
    if DataBase:
        averages = calculate_average(DataBase) 
        for eachuser in DataBase:
            print(f"\nName: {eachuser['Name']}")
            print(f"Average Score: {averages[eachuser['Name']]:.2f}")
            print(f"Admin Access: {hasAdminAccess(eachuser['Roles'])}")




 #   print(DataBase)


main()