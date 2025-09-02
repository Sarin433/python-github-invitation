import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Setting up API URL and headers
upn = pd.read_csv("./name.csv")

api_url = os.getenv("api_url")

headers = {
    "Authorization": os.getenv("Authorization"),
    "X-GitHub-Api-Version": os.getenv("X-GitHub-Api-Version"),
    "Accept": os.getenv("Accept")
}

# write post request to github org invitations
for user in upn["upn"]:
    body = {
        "email": f"{user}",
        "role": "direct_member"
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(body))

    if response.status_code == 201:
        print("Invitation sent successfully.")
    else:
        print(f"Failed to send invitation: {response.status_code}")
        print(response.json())