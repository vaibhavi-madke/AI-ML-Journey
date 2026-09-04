import pandas as pd

data = {
    "Name"  : ["Justin","Elena","Sumedh","Allie","Dean","Joe","Devil"],
    "Age"   : [19, 20, 19, 21, 20, 19, 22],
    "Maths" : [85, 92, 78, 95, 88, 65, 97],
    "Python": [90, 88, 82, 91, 85, 70, 98],
    "AI"    : [88, 94, 79, 93, 87, 68, 95],
    "City"  : ["Pune","Mumbai","Delhi","Pune","Mumbai","Delhi","Pune"]
}
df = pd.DataFrame(data)

# ---- Selecting columns ----
print("=== Single Column ===")
print(df["Name"])

print("\n=== Multiple Columns ===")
print(df[["Name", "Maths", "Python"]])

# ---- Selecting rows ----
print("\n=== Row by index (iloc) ===")
print(df.iloc[0])        # first row
print(df.iloc[1:4])      # rows 1 to 3

print("\n=== Row by label (loc) ===")
print(df.loc[df["Name"] == "Priya"])

# ---- Filtering rows with conditions ----
print("\n=== Students from Pune ===")
print(df[df["City"] == "Pune"])

print("\n=== Maths above 85 ===")
print(df[df["Maths"] > 85][["Name", "Maths"]])

print("\n=== Pune students scoring 85+ in Python ===")
filtered = df[(df["City"] == "Pune") & (df["Python"] >= 85)]
print(filtered[["Name", "City", "Python"]])

# ---- Adding new columns ----
df["Average"] = (df["Maths"] + df["Python"] + df["AI"]) / 3
df["Average"] = df["Average"].round(1)

df["Grade"] = df["Average"].apply(lambda x:
    "A+" if x >= 90 else
    "A"  if x >= 80 else
    "B"  if x >= 70 else "C")

df["Status"] = df["Average"].apply(
    lambda x: "Pass ✅" if x >= 60 else "Fail ❌")

print("\n=== Updated DataFrame ===")
print(df[["Name", "Maths", "Python", "AI", "Average", "Grade", "Status"]])

# ---- Sorting ----
print("\n=== Sorted by Average (Best first) ===")
print(df.sort_values("Average", ascending=False)[
      ["Name","Average","Grade"]].reset_index(drop=True))