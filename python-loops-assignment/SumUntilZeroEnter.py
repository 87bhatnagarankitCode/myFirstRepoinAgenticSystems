sum = 0
while True:
    try:
        input_number = int(input(" enter numebr of ur choice : "))
        if input_number == 0:
             break
        else:
            sum += input_number
    except ValueError: 
        print("     Incorrect value, enter Numeric value only    ") 
print("Total : ",sum)        