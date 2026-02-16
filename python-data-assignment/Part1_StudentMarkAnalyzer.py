

def inputStudentMarks():
    Marks =[]
    print(" --- Enter atleast 8 student's marks ---")
    while True:
        counter = len(Marks)
        try:
            mark = float(input(f"\n enter the marks of student {counter + 1}  : "))
            if mark > 100:
                print("\n Incorrect value, Marks must be under 100. Reenter Please")
            else:     
                Marks.append(mark)
        except ValueError:
            print(" Incorrect value, reenter mark for this student")
    #return Marks    
        if (len(Marks) >= 8):
            if (Ch :=  input(f" Do you want to continue ? Yes,YES or 'Y'. Press any other key to stop :: ").lower() not in ("yes","y") ) :
                break
        
    return Marks

def DisplayOutput(Marks):
    print(f"\n  The full Marks list : {Marks}")
    print(f"     The first 3 marks : {Marks[0:3]}")
    print(f"     The last 3 marks  : {Marks[-3:]}")


def DisplayManipuatedData(mList):
    print(" \n ----------------------- Sumary ------------------------")
    print(f"Highest mark : {max(mList)}")
    print(f"Lowest  mark : {min(mList)}")
    print(f"Average mark : {(sum(mList)/len(mList)):.2f}")
    


def main():
    ListofMarks = inputStudentMarks()
    DisplayOutput(ListofMarks)
    DisplayManipuatedData(ListofMarks)


main()