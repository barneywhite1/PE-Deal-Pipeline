import os
import csv
import requests
from dotenv import load_dotenv

# Load the API key
load_dotenv()
api_key = os.getenv("CH_API_KEY")

url = "https://api.company-information.service.gov.uk/advanced-search/companies"
page_size = 5000          # most Companies House allows per request
start = 0                 # where the current page starts
all_companies = []        # empty list to collect everything in

# ----- Keep asking for pages until there are none left -----
while True:
    search_filters = {
        "sic_codes": "75000",
        "company_status": "active",
        "size": page_size,
        "start_index": start,
    }
    response = requests.get(url, auth=(api_key, ""), params=search_filters)

    if response.status_code != 200:
        print("Something went wrong:", response.text)
        break

    items = response.json().get("items", [])
    all_companies.extend(items)
    print(f"Got {len(items)} companies (total so far: {len(all_companies)})")

    # If this page wasn't full, it was the last one
    if len(items) < page_size:
        break

    start = start + page_size

# ----- Save everything into a CSV file -----
with open("vets.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["company_number", "company_name", "date_created", "town", "postcode", "sic_codes"])

    for company in all_companies:
        address = company.get("registered_office_address", {})
        writer.writerow([
            company.get("company_number"),
            company.get("company_name"),
            company.get("date_of_creation"),
            address.get("locality"),
            address.get("postal_code"),
            ", ".join(company.get("sic_codes", [])),
        ])

print(f"Saved {len(all_companies)} companies to vets.csv")