import pandas as pd
from sqlalchemy import create_engine, text

# Log file to track issues
log_data = []

# Step 1: Extract - Read raw data from CSV
def extract(file_path):
    df = pd.read_csv(file_path)
    return df

# Step 2: Analyze & Log Issues
def log_issue(row_index, column, issue, fix):
    log_data.append({"Row": row_index, "Column": column, "Issue": issue, "Fix": fix})

# Step 3: Transform - Data Cleaning
def transform(df):
    # Trim spaces from column names & values
    df.columns = df.columns.str.strip()
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    # Handle duplicate rows
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        df.drop_duplicates(inplace=True)
        log_issue("All", "Duplicates", f"{duplicate_count} duplicate rows found", "Removed duplicates")

    # Fix incorrect city names
    city_mapping = {"Dehli": "Delhi", " Pune": "Pune", "Hydrabad": "Hyderabad"}
    df["city"] = df["city"].replace(city_mapping)

    # Handle unknown cities
    known_cities = ["Delhi", "Mumbai", "Bangalore", "Pune", "Kolkata", "Chennai", "Hyderabad"]
    unknown_cities = df[~df["city"].isin(known_cities)]
    for index, row in unknown_cities.iterrows():
        log_issue(index, "city", f"Unknown city: {row['city']}", "Set to 'Unknown'")
        df.at[index, "city"] = "Unknown"

    # Fix amount column (convert to float, handle missing & negative values)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0).abs()
    df.loc[df["amount"] > 100000, "amount"] = 100000  # Cap outliers
    log_issue("All", "amount", "Handled missing, negative, and outlier values", "Converted to float, replaced NaN, capped outliers")

    # Fix date column
    df["processed_at"] = pd.to_datetime(df["processed_at"], errors="coerce")
    df.loc[df["processed_at"].isna(), "processed_at"] = pd.Timestamp("2000-01-01")

    # Validate email addresses
    df["email"] = df["email"].apply(lambda x: x if isinstance(x, str) and "@" in x and "." in x else "")
    invalid_emails = df[df["email"] == ""]
    for index, row in invalid_emails.iterrows():
        log_issue(index, "email", "Invalid email format", "Set to blank")

    # Drop rows with missing names
    df = df[df["name"].str.strip() != ""]

    # **Remove remaining duplicates based on relevant columns**
    df = df.drop_duplicates(subset=["name", "city", "amount", "processed_at", "email"])

    return df


# Step 4: Load - Store cleaned data into PostgreSQL
def load(df, db_uri, table_name):
    engine = create_engine(db_uri)
    
    with engine.connect() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print("Cleaned data loaded successfully.")

        # **Delete remaining duplicates from database**
        delete_query = text(f"""
            DELETE FROM {table_name} 
            WHERE ctid NOT IN (
                SELECT min(ctid) 
                FROM {table_name} 
                GROUP BY name, city, amount, processed_at, email
            )
        """)
        conn.execute(delete_query)
        conn.commit()


# Step 5: Generate Data Quality Report
def generate_report():
    report_df = pd.DataFrame(log_data)
    report_df.to_csv("data_quality_report.csv", index=False)
    print("Data quality report saved as data_quality_report.csv")

# Running the ETL pipeline
if __name__ == "__main__":
    file_path = "raw_messy_data.csv"
    db_uri = "postgresql://postgres:Bsk123@localhost:5433/Learn"
    table_name = "cleaned_data"

    df = extract(file_path)
    print("Raw Data:\n", df)

    df = transform(df)
    print("Transformed Data:\n", df)

    load(df, db_uri, table_name)

    generate_report()
