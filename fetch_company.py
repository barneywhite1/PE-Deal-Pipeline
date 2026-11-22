import os
import requests
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("CH_API_KEY")

# The company to look up (00445790 is Tesco PLC)
company_number = "00445790"
url = f"https://api.company-information.service.gov.uk/company/{company_number}"

# Ask Companies House for the data
response = requests.get(url, auth=(api_key, ""))
print(f"Status code: {response.status_code}")

# Show the results, or the error if something went wrong
if response.status_code != 200:
    print("Something went wrong:", response.text)
else:
    data = response.json()
    print(f"Name: {data['company_name']}")
    print(f"Status: {data['company_status']}")
    print(f"Incorporated: {data['date_of_creation']}")
    print(f"Industry codes (SIC): {data.get('sic_codes')}")