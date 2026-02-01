
UserName = input("\n Please Enter you name :")
Age      = input("\n Please Enter your age :")
IsActive = input("\n Are you actve user. Please enter (True / False):")



if not ( Age.isnumeric() and (IsActive.lower() in ["true" ,"false"])):
    print(" **** Enter correct details please ****")
else:
     if (IsActive.lower() == "true"):
         IsActive = True
     elif  (IsActive.lower() == "false"):
         IsActive = False
     print(f"User {UserName} is {Age} years old. Active status: {IsActive}")