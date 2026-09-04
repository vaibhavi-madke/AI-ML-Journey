import pandas as pd
import numpy as np

# ===== SERIES — 1D labelled array =====
# Like a single column of a spreadsheet

marks = pd.Series([85, 92, 78, 95, 88],
                  index=["Maths", "Python", "AI", "Stats", "Physics"])

print("=== My Marks (Series) ===")
print(marks)
print("\nData type  :", marks.dtype)
print("Shape      :", marks.shape)
print("Maths marks:", marks["Maths"])
print("Above 85   :\n", marks[marks > 85])
print("Average    :", marks.mean())

# ===== DATAFRAME — 2D table (rows + columns) =====
# Like a full spreadsheet — this is what you'll use 99% of the time

data = {
    "Name"    : ["Rohan","Priya","Aman","Sneha","Raj","Meera","Dev"],
    "Age"     : [19, 20, 19, 21, 20, 19, 22],
    "Maths"   : [85, 92, 78, 95, 88, 65, 97],
    "Python"  : [90, 88, 82, 91, 85, 70, 98],
    "AI"      : [88, 94, 79, 93, 87, 68, 95],
    "City"    : ["Pune","Mumbai","Delhi","Pune","Mumbai","Delhi","Pune"]
}

df = pd.DataFrame(data)

print("\n=== Class DataFrame ===")
print(df)

# ---- First look at any dataset (do these ALWAYS) ----
print("\n=== Dataset Info ===")
print("Shape      :", df.shape)       # rows, columns
print("Columns    :", list(df.columns))
print("\nFirst 3 rows:\n", df.head(3))
print("\nLast 2 rows:\n", df.tail(2))
print("\nData types:\n", df.dtypes)
print("\nBasic stats:\n", df.describe())