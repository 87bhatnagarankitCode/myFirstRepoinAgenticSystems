import requests
import os

url = "https://api.example.com/data"




def fetchEnvKeys():
    Keys = os.getenv("Secure_API_Keys")

    if not Keys:
        print("Error: API_KEY environment variable not set.")
        return
    headers = {
        "Authorization": f"Bearer {Keys}"
    }
    return headers



def main():
    Headers = fetchEnvKeys()
    if Headers:
        try:
            response = requests.get(url,headers=Headers)
            if response.status_code == 200:
                print("Approved", response.json())
            elif response.status_code == 429:
                print("Rate limit reached. Try again later.")
            else:
                print("Request failed >>  ", response.status_code)
        except Exception as ex:
            print(f" Exception occured  {ex}")

