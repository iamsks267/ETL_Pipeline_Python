import pandas as pd

# Creating raw data with multiple issues
data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11],  # Duplicate ID (8)
    "name": [" Alice", "Bob ", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Helen", "", "John", "  "],  # Extra spaces & missing name
    "city": ["Delhi", "Dehli", "Mumbai", " Pune", "Bangalore", "Kolkata", "Chennai", "Hyderabad", "Hydrabad", "NYC", "  ", "Bangalore"],  # Incorrect spellings & unknown city
    "amount": ["100", "200.5", "N/A", "450", "-300", "250", "NaN", "400", "400", "500000", "700", "550"],  # Negative, missing, & outlier values
    "processed_at": ["2024-01-01", "2024-02-02", "N/A", " ", "2024-05-06", "2024-06-07", "2024-14-32", "2024-08-09", "2024-08-09", "2024-10-11", "2025-13-01", " "],  # Incorrect & missing dates
    "email": ["alice@mail.com", "bob123@", "charlie@email.com", "david@domain", "eve@work.com", "frank@", "", "helen@mail.com", "helen@mail.com", "invalid.com", "john@", " "]  # Invalid emails
}

df = pd.DataFrame(data)

# Save raw data to CSV
df.to_csv("raw_messy_data.csv", index=False)
print("Raw messy data saved as raw_messy_data.csv")