
import pandas as pds
import os

os.system('cls')

path_prefix = r"C:\Users\91916\Downloads\Masai\Assignment1\myFirstRepoinAgenticSystems\myFirstRepoinAgenticSystems\python-logic-assignment"

data = {
    "StudentID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
    "Stream": ["BIO", "MATHs", "BIO", "BIO", "MATHs", "MATHs", "BIO", "MATHs"],
    "Age": [21, 22, 21, 20, 23, 22, 24, 21],
    "Score": [80, 93, 64, 98, 46, 93, 72, 83],
    "Grade": ["A", "A++", "B", "A++", "C", "A++", "B++", "A"],
    "PassedCutoff": [False, True, False, True, False, True, False, False],
    "Labels": ["A", "B", "C", "D", "E", "F", "G", "H"]
}

def printOutput(df):
    print("First 5 rows: \n",df.head())
    print("Last 5 rows: \n",df.tail())
    print("Dataset Info: \n",df.info())
    print("Summary Statistics: \n", df.describe())
    age = df["Age"]
    print("Age>>\n"+ str(age))
    multiple_col = df[["Name","Age","Stream","Grade","PassedCutoff"]]
    print("multiple_col \n" + str(multiple_col) )

    #filtered = df[df["Score"] > 80]
    filtered = df["Score"] > 80
 #   print("Students more then '80' :" , filtered) # prints True/False
 
    print("Students names more then '80' : \n",df.loc[df["Score"] > 80, ["StudentID","Name","Score"]])


def hardcodeDataset():
    df = pds.DataFrame(data)
    printOutput(df)

def UseExternalCSV():
    df = pds.read_csv(path_prefix+r"\StudentsDataSet.csv")
    printOutput(df)

def main():
    while True:
        Ch = input("input choices Press (1)- DataSet from CSV (2)- Dataset within program (3)- Exit    >> " ).strip()
        if Ch not in ["1","2","3"]:
            print("Wrong Choice, TRY AGAIN !!")
        else:
            if Ch == "3":
                break
            elif Ch == "2":
                hardcodeDataset()
            else:
                UseExternalCSV()
           

main()