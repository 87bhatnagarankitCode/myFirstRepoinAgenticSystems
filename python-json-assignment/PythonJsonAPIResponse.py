import json
import os,sys


os.system('cls')
jsonPredefined = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''



def AccpetJSONResponse():
  #  userJSONrespnse = input(" Please input JSON response : \n")
    print("\n Please input JSON response. Press 'ctrl + Z (case sensitive)  + Enter'  ,when finished")
    userJSONrespnse = sys.stdin.read()
    try:
        JSONrespnse = json.loads(userJSONrespnse) 

        print(" ***** Input JSON has been parsed properly **** ")
        return JSONrespnse
    except json.JSONDecodeError:
         print(" Not a proper JSON format")
         return None

def ExtractInfo(JSONrespnse):
    try:
        request_id = JSONrespnse.get("id")
        status     = JSONrespnse.get("status")
        
        result     = JSONrespnse.get("result")
        text       = result.get("text")
        confidence = result.get("confidence")
        print(f"Request ID: {request_id}")
        print(f"Status: {status}")
        print(f"Text: {text}")
        print(f"Confidence: {confidence}")
        if confidence < 0.9:
            print(" !!!!Warning!!!! Confidence score is below threshold!")
    except KeyError:
        print("  key not found")


def WriteFollowUp(JsonToWrite):
    with open("response.json", "w") as f:
         json.dump(JsonToWrite, f, indent=4)
         print("File written successfully!")

   

def main():
    while True:
        ch = input(" Enter your choice. press 1- Use Predfeined Json, 2- Input JSON, 3- Quit. >> ")
        if ch not in ["1","2","3"]:
            print(" *** Invalid choice ***")
        else:       
            if ch == "3":
                print("\n *** Quiting...... ***")
                break
            elif ch =="1":
                print("\n **** Proceeding with Predefined Json ****")
                ExtractInfo( json.loads(jsonPredefined))
                WriteFollowUp(json.loads(jsonPredefined))
                break
            else:
                JSONrespnse = AccpetJSONResponse()
                if JSONrespnse :
                    ExtractInfo(JSONrespnse)
                    WriteFollowUp(JSONrespnse)
                else:
                    print(" Not a proper request.. Exiting.....")
                break
    

main()