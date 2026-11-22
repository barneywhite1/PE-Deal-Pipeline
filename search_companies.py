import os 
import requests
from dotenv import load_dotenv

#Supposed to load the API key from the .env file
load_dotenv()
api_key = os.getenv("CH_API_KEY")

#What I am looking for in particular, as in the filter. This example is aimed at vets, that are still currently trading companies.
url = "https://api.company-information.service.gov.uk/advanced-search/companies"
search_filters = {
    "sic_codes": "75000",        # vets
    "company_status": "active",  # still trading
    "size": 20,                  # how many results to return
}

#Next is to ask Companies House
response = requests.get(url, auth=(api_key, ""), params=search_filters)
print(f"Status code: {response.status_code}")

if response.status_code !=200:
    print("Something went wrong")
else:
    data = response.json()
    print(f"Total matches: {data['hits']}")
    print()


    #Go through each company in the resutls
    for company in data["items"]:
        name = company["company_name"]
        number = company["company_number"]
        print(f"{number}  {name}")