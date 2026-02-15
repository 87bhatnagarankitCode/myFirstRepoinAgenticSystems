import os
from datetime import datetime

os.system('cls')

def Ts():
    return datetime.now().isoformat(sep=" ", timespec="milliseconds")



def GetFilesLocation():
    print(" PLEASE ENTER FILE LOCATIONS. IN CASE LOG FILE LOCATION IS SAME, JUST PRESS ENTER ONLY")
    print("==" * 50)
    while True:
        LocationReadFile = input("\n Enter 'Read File' location (full path): " ).strip()
        LocationLogFile  = input("\n Enter 'Log File' location (full path): " ).strip()
        if LocationReadFile == "":
            print("---->> Read File Path MUST be provided. Renter Please.")
        else:
            if LocationLogFile =="" :
                print("---->>Log File Path is not be provided.")   
                print("---->>Log file will be created in the 'Read File' location")
                return (rf"{LocationReadFile}", rf"{LocationReadFile}")
            else:
                print("---->>Both locations are separate.")
                return(rf"{LocationReadFile}",rf"{LocationLogFile}")
                 
def GetFilesNames():
    while True:
        ReadFileName     = input("\n Enter 'READ File' Name: " ).strip()
        LogfileName     = input("\n Enter 'LOG File'  Name: " ).strip()
        if ReadFileName == "":
            print("---->> Read File NAME MUST be provided. Renter Please.")
        else:
            if not os.path.splitext(ReadFileName)[1]:
                print(f"---->> Extension of READ File is not presnt. Appending .txt as extension")
                ReadFileName = ReadFileName + ".txt"
            if LogfileName == "":
                LogfileName =  os.path.splitext(ReadFileName)[0] + ".log"  # changing extension
                print(f"---->> Log File NAME is not provided. Default {LogfileName} will be used.")
             
            return (ReadFileName, LogfileName)


def openfilesProcessItems(ReadFileName, LogFileName):
    try:
        with open(LogFileName, "a") as logfile:
            try:
                with open(ReadFileName, "r") as readfile:
                    logfile.write("\n"+"##"*50)
                    logfile.write(f"\n{Ts()} File opened successfully")
                    wholeListofNumbers = ProcessItems(logfile,readfile)
                    logfile.write(f"\n{Ts()} Read {len(wholeListofNumbers)} numbers")
                    logfile.write(f"\n{Ts()} Sum {sum(wholeListofNumbers)} ")
                    logfile.write(f"\n{Ts()} Average {float(sum(wholeListofNumbers)/len(wholeListofNumbers) if wholeListofNumbers else 0)} ")
                    logfile.write(f"\n{Ts()} Processing Complete ")
                    print("\n ****##**## Please check the Log File for the details. ****##**## ")
            except FileNotFoundError:
                print("---->> Read File Does Not exist !!!!!")
                logfile.write(f"\n{Ts()} *** Read File Not Found ****")
                ProcessItems(logfile,None)
    except FileNotFoundError:
        print("\n---->> ******** Entered Directory path is wrong. Exiting. Kindly correct and ReRun. ******** ")
        print("---->>  Log file couldnt be created due to incorrect directory path")
def ProcessItems(logfile,readfile):
    if readfile is None:
        logfile.write(f"\n{Ts()} Processing won't take place")
    else:
        logfile.write(f"\n{Ts()} About to read Read File ")
        wholeListofNumbers =[]
        for eachline in readfile:
            if eachline:
                try:
                    integerVal = int(eachline.strip())
                    wholeListofNumbers.append(integerVal)
                except ValueError:
                  #  print(" Not an integer ;skipping this line")
                    logfile.write(f"\n{Ts()} Non Integer Found in Read File, skipping this line")
        return wholeListofNumbers
        



def main():
    ReadFileLoc, LogFileLoc = GetFilesLocation()
    ReadName, LogName = GetFilesNames()
 #   print(" Read File Location : ", ReadFileLoc)
 #   print(" Log  File Location : ", LogFileLoc)
    ReadFullPath = rf"{ReadFileLoc}\{ReadName}"
    LogFullPath  = rf"{LogFileLoc}\{LogName}"
    print("\n ---->> Reading from : \n", ReadFullPath )
    print("\n ---->> Logging file path : \n", LogFullPath)
    openfilesProcessItems(ReadFullPath,LogFullPath)
    print("\n #### End of Processing ####")

main()