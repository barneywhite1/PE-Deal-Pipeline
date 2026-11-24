import pandas as pd

# Load the CSV into a table
df = pd.read_csv("vets.csv", dtype=str)

print(f"Starting companies: {len(df)}")
print()
print(df.head())

# This filters the the SIC codes, for just the vet industry
df = df[df["sic_codes"]  == "75000"]
print()
print(f"After filter 1 (vet code only): {len(df)}")


#Second Filter: This searchs for companies that are at least five years old, 
df["date_created"] = pd.to_datetime(df["date_created"])
cutoff = pd.Timestamp.today() - pd.DateOffset(years=5)
df = df[df["date_created"] <= cutoff]
print(f"After filter 2 (5+ years old): {len(df)}")

#Third Filter: Drop obvious non-vets by name. Reason being this filter tends to include a of dog carers and walkers
not_vet_words = ["GROO", "DOG", "FARRIER", "SITTER", "LOCUM", "KENNEL", "CATTERY", "TRAINING", "HYDROTHERAPY", "PET CARE"]

pattern = "|".join(not_vet_words)
df = df[~df["company_name"].str.contains(pattern, case=False)]
print(f"After filter 3 (obvious non-vets removed): {len(df)}")

#Save the screened list
df.to_csv("vets_screend.csv", index=False)
print("Saved to vets_screened.csv")