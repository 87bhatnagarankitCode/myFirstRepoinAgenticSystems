import os

os.system('cls')
current_year =2026
birth_Year   = 0
try:
    birth_Year   = int(input(" Please Enter your 'Birth year' : "))
    if not (birth_Year <= 0 or birth_Year > current_year):
        print(f"You are {current_year - birth_Year} years old.")
    else: 
        print("******Invalid input. Birth year can not be a 'future year', '0' or '-' . ******")

except ValueError:
     print("******Invalid input. Please enter a numeric value.******")

