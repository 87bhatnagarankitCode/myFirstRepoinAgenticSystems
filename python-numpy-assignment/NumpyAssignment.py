
import numpy as np

def performOperation(UserList):
    numpyarray = np.array(UserList)
    print("Original Data : ", numpyarray)
    #mean
    mean = numpyarray.mean()
    print("Mean : ", mean )
    
    std = numpyarray.std()
    print("Standard Deviation : ", std)

    normalized = (numpyarray - mean ) / std
    print("Normalized data : ", normalized)
    sizeOfArray = numpyarray.size
    quotient, remainder = divmod(sizeOfArray ,2)
    if remainder  == 0:
        reshaped_2Darray = numpyarray.reshape(2,quotient)

    else:
        reshaped_2Darray = numpyarray.reshape(1, sizeOfArray)
    print("Reshaped data : ",reshaped_2Darray)
    print("Reshaped data shape : ", reshaped_2Darray.shape)

def main():
    UserList = UserInput()
    performOperation(UserList)
    

def UserInput():
    InputList =[]
    while True:
        print("--"*50)
        InputVals = input(" Please enter values separated by ';'. ** DO NOT ADD ';' AFTER LAST NUMBER. ** press q/Q to quite : ")
        print("--"*50)
        if (InputVals.strip() in ["q","Q"]) :
            print("Quiting....")
            break
        try:
            tempInputList = InputVals.split(";")
            InputList = [float(value.strip()) for value in tempInputList]
            return InputList

        except ValueError:
            print("Wrong input.")

  
main()
