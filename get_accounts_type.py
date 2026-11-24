import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

# Load the API key
load_dotenv()
api_key = os.getenv("CH_API_KEY")

# Load the screened list, and test on the first 20 only
df = pd.read_csv("vets_screened.csv", dtype=str)
df = df.head(20)

accounts_types = []   # empty list to collect the answers

for number in df["company_number"]:
    url = f"https://api.company-information.service.gov.uk/company/{number}"
    response = requests.get(url, auth=(api_key, ""))

    if response.status_code == 200:
        data = response.json()
        acc_type = data.get("accounts", {}).get("last_accounts", {}).get("type")
    else:
        acc_type = None

    accounts_types.append(acc_type)
    print(number, acc_type)
    time.sleep(0.5)

# Add the answers as a new column and save
df["accounts_type"] = accounts_types
df.to_csv("vets_with_accounts.csv", index=False)
print("Saved to vets_with_accounts.csv")