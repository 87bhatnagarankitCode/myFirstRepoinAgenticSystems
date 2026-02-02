passingMarks    = 50
_MAXIMUM_         = 100
inputMarksStr   = input("Please enter the marks : ")
#if (inputMarksStr.isnumeric()):
#     inputMarks = int(inputMarksStr)
#     if (inputMarks > _MAXIMUM_):
#          print("Invaid! Input given exceeds the max marks.")
#     elif (inputMarks >= passingMarks):
#          print("Pass")
#     else:
#         print("Fail")     
#else:
#     print("Invalid Input value. Please enter valid marks ")

###### above logic doesnt handle '-' negative marks ..Rewriting below logic with try except

try:
     inputMarks = int(inputMarksStr)
     if (inputMarks > _MAXIMUM_):
          print("Invaid! Input given exceeds the max marks.")
     elif (inputMarks >= passingMarks):
         print("Pass")
     else:
         print("Fail")     

except ValueError:
     print("Invalid Input value. Please enter valid marks ")