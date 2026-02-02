#2.3 Secure Transaction Validator


try:
    statusVerified = False
    accountBalance = int(input( "Please enter ACCOUNT BALANCE  : "))
    withdrawlAmt   = int(input( "Please enter WITHDRAWL AMOUNT : "))
    statusVerify   = input("Are you verified? (True/False) : ")
    if (statusVerify.lower() == "true" or statusVerify.lower() == "yes"  or 
        statusVerify.lower() == "y"    or statusVerify.lower() == "t"  ):
        statusVerified = True
    
    if (statusVerified and withdrawlAmt <= accountBalance ):
        print("Withdrawal successful")
    else:
        print("Withdrawal Unsuccessful")    

except ValueError:
    print("Please correct the entered Amount")
