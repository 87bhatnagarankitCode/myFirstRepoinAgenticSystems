
import os
os.system('cls')

try:
    input_accuracy = float(input("Please enter the floating-point accuracy value : "))
    print(f"Model accuracy is {input_accuracy}")
except ValueError:
    print(" ***** Invalid Input!! Entered value is  non nueric ***** ")

''' below logic has a limitation it cannot accept  in  negative

'''



#input_accuracy = input("Please enter the floating-point accuracy value : ")
#if (input_accuracy.isnumeric()):
#     print(f"Model accuracy is {float(input_accuracy)}")   
#else :
#     print("***** Invalid Input!! Entered value is  non nueric *****")    
  

