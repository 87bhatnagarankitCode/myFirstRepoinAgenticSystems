import pandas as pd
import os

os.system('cls')
path_prefix = r"C:\Users\91916\Downloads\Masai\Assignment1\myFirstRepoinAgenticSystems\myFirstRepoinAgenticSystems\python-logic-assignment"


def loadDataSet():
    loadeddf = pd.read_csv(path_prefix+r"\StudentsDataSet.csv")
    return loadeddf

def performOperations(df):
    #select single column and print it
    Columns = df.columns.to_list()
 #   print(type(Columns))
    print(df[Columns[0]])
    print(df[[Columns[0],Columns[1],Columns[5]]])
    newDF = df[[Columns[0],Columns[1],Columns[2], Columns[4],Columns[5]]]
    print("New DataFrame >> \n" ,newDF)
    print("1st 3 rows using iloc :\n", newDF.iloc[0:3])
    lableDF = df.set_index("Labels")
    print("-------------------------Using loc : \n")
    print(lableDF.loc["A"]," ******** ",type(lableDF.loc["A"]))
    print(lableDF.loc[["A","B"]]," ******** ",type(lableDF.loc[["A","B"]]))
    print(lableDF.loc["A":"E"]," ******** ",type(lableDF.loc["A":"E"]))
    print("Column seection: \n",lableDF.loc["A":"E",["StudentID","Name","Stream"]]," ******** ",type(lableDF.loc["A":"E",["StudentID","Name","Stream"]]))
    print("*"*25, "Filtering","*"*25,"\n")
    filterDF = df["Score"] > 85
    print("Only prints boolean  series ",filterDF, "\n", " Fileterd : \n ",df[filterDF])
    mixedFilter = df[(df["Score"] > 85) & (df["PassedCutoff"])]
    print("High-performing students (Score > 85 and Passed ) :  \n", mixedFilter)
    print("Sorted high performers (descending by scores ) : \n", mixedFilter.sort_values("Score",ascending=False))

def main():
    df = loadDataSet()
    performOperations(df)



main()