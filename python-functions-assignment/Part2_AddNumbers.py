def inputNumbers():
    while True:
        try:
            Num1 = int(input(" Please enter \033[1m1st\033[0m number : "))
            break 
        except ValueError:
            print("!!! Entered numercial value is wrong !!!")      
         
    while True:
        try:
            Num2 = int(input(" Please enter \033[1m2nd\033[0m number : "))
            break
        except ValueError:
            print("!!!! entered numercial value is wrong !!!!")            
        
    return [Num1, Num2]  

def addition(n1,n2):
    return n1+n2

def printsum():
    ListOfInputNumbers = inputNumbers()
    
    print(f" \033[1msum is :\033[0m {addition(ListOfInputNumbers[0],ListOfInputNumbers[1])}")

printsum()    