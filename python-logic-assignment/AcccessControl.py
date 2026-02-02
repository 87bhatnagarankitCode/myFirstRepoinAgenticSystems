#2. Access Control System


age = input(" Please enter your age : ")
hasID = False
adultAge = 18

if (not age.isnumeric()):
    print("Entered age is INCORRECT")
else:
     hasIDStr = input(" Please confirm if you have ID Card - (True/False)  : ")  
     if (hasIDStr.lower() == "true" or hasIDStr.lower() == "yes" or 
         hasIDStr.lower() == "y"    or hasIDStr.lower() == "t" ):
          hasID = True
     if (hasID and int(age) >= adultAge):
          print("Entry allowed")
     else:
          print("Entry NOT allowed")

 