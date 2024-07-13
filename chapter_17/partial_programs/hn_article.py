import requests
import json


# Make an API call, and store the response.
url = "https://mycontainerapp.niceforest-8dcb0da3.eastus.azurecontainerapps.io/"
# /

r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)