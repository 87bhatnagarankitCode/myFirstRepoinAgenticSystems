import requests
import json
import os

os.system('cls')
url = "https://api.github.com/search/repositories"

response = requests.get(url,params={"q":"python","sort":"stars","order": "desc","per_page": 2})


print("="*50) 
print(json.dumps(response.json(),indent=4))
print( [ f"{repo['name']} -> {repo['stargazers_count']} stars" for repo in response.json()['items']])


