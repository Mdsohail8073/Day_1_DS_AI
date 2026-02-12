# -*- coding: utf-8 -*-

#author : acer 
# STEP 1 — Import pandas
import pandas as pd

# STEP 2 — Create messy dataset (added Date + messy City + duplicate row)
data = {
    "CustomerID": [101,102,103,104,105,106,107,107,108,109],
    "Name": ["Amit","Sara","John",None,"Priya","David","Meena","Meena","Ali","Riya"],
    "Age": [25,None,30,22,None,28,35,35,None,26],
    "City": [" Bangalore","Mumbai ","Delhi",None,"Bangalore","Chennai","Mumbai","Mumbai","Delhi"," Bangalore "],
    "OrderAmount": [2500,1800,None,2200,3000,None,1500,1500,2700,None],
    "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"],
    "Date": ["2024-01-05","2024-01-10","2024-02-01","2024-02-05","2024-03-01",
             "2024-03-05","2024-03-10","2024-03-10","2024-04-01","2024-04-05"]
}

df = pd.DataFrame(data)

# STEP 3 — Inspect dataset
print("First rows:\n", df.head())
print("\nDataset info:")
print(df.info())

# STEP 4 — Check missing values
print("\nMissing values per column:")
print(df.isna().sum())

# STEP 5 — Fill missing values (statistical approach)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])
df["Name"] = df["Name"].fillna("Unknown")

# STEP 6 — Check data types before conversion
print("\nData types BEFORE conversion:")
print(df.dtypes)

# STEP 7 — Convert data types
df["Age"] = df["Age"].astype(int)
df["Date"] = pd.to_datetime(df["Date"])

print("\nData types AFTER conversion:")
print(df.dtypes)



#Task1
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("imam.csv")

# Shape before cleaning
print("Shape before cleaning:", df.shape)

# 2. Report missing values
print("\nMissing values report:")
print(df.isna().sum())

# 3. Fill missing numeric values with median
numeric_columns = df.select_dtypes(include=["number"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# 4. Remove duplicate rows (across all columns)
df = df.drop_duplicates()

# Shape after cleaning
print("\nShape after cleaning:", df.shape)

#Task 2
import pandas as pd

# Load the dataset
df = pd.read_csv("imam.csv")

# 1. Check initial data types
print("Initial data types:")
print(df.dtypes)

# 2. Remove '$' symbol and convert amount to float
df["amount"] = (
    df["amount"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .astype(float)
)

# 3. Convert Date column to datetime (change column name if needed)
df["date"] = pd.to_datetime(df["date"])

# Check data types after conversion
print("\nData types after conversion:")
print(df.dtypes)

#Task3
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK ", "New York"]
})

# 1. Remove leading/trailing whitespace
# 2. Standardize casing (use .str.title() or .str.lower())
df["Location"] = df["Location"].str.strip().str.title()

# 3. Verify the fix
print(df["Location"].unique())



