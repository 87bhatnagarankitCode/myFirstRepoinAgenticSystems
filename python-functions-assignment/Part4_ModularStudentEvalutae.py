def InputStudentName():
    while True:
        name = input("\n Enter Student name : ").strip()
        if name == "":
            print(" Please enter proper name ")
        else:
            return name
        


def acceptMarksProperInput():
    while True:
        if (finalList := acceptMarks()):
             return finalList
            
    
                  
def acceptMarks():
    Inputlistofmarks = input(" Please enter marks separated with pipe sign e.g. 75|90|8 = ").split("|")
    listofmarks =[]
    length = len(Inputlistofmarks)
    i = 0
    for mark in Inputlistofmarks:
        i += 1
        if mark.strip() != "":
            try:
                if (float(mark) > 100):
                    print(" Subject Marks can not exceed 100")
                    return []
                listofmarks.append(float(mark))
                      
            except ValueError:
                print(" Incorrect numeric input value")
                return []
        else:
            print(" wrong input of marks")
    return listofmarks            
    
def generateResult(ListofMarks):
    total = 0
    result =""
    if  ListofMarks:
         for mark in ListofMarks:
             total += mark
         average = total/len(ListofMarks)
        # print(f" Average Score: {average:.2f}") # format result upto 2 digits only
         if average >=  50:
             #print(" Result: Pass")
             result = "Pass"
         else:
             #print(" Result: Fail")
             result = "Fail"
         return average, result
    else:
        print(" Error!!!! Marks list is empty")
        return 0,"Error"


def main():
       
    print(f" Hello, {InputStudentName()} ")     
    FloatingList = acceptMarksProperInput()
    print(f" Subjects : {len(FloatingList)}")
    Avergae, Result = generateResult(FloatingList)
    print(f" Average Score: {Avergae:.2f}")
    print(f" Result: {Result}")
  #  print(FloatingList)
    


if __name__ == "__main__":
    main()
