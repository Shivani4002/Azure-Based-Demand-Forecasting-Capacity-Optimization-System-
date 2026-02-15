import pandas as pd
import matplotlib.pyplot as plt

# ---------------- LOAD DATA ---------------- #
df = pd.read_csv(r"C:\CODING\PandasApp\azure_synthetic_dataset_5000.csv")


# Use only first 50 rows for testing
# df = df.head(50)

# Clean column names
df.columns = df.columns.str.strip()

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# ---------------- HANDLE NULLS ---------------- #
# Drop rows with nulls in important columns
important_cols = [
    "timestamp", "region", "service_type", "units_used",
    "provision_capacity", "availability", "cost_use",
    "external_holiday", "internal_maintenance"
]
df = df.dropna(subset=important_cols)

# Remove duplicates
df = df.drop_duplicates()

# ---------------- CASE HANDLING ---------------- #
# RAW columns (original)
df["region_raw"] = df["region"]
df["service_type_raw"] = df["service_type"]

# CANONICAL columns (cleaned)
df["region_canonical"] = df["region"].str.strip().str.title()
df["service_type_canonical"] = df["service_type"].str.strip().str.title()

# ---------------- PRINT RAW vs CANONICAL ---------------- #
print("\n===== REGION: RAW vs CANONICAL =====")
print(df[["region_raw", "region_canonical"]].drop_duplicates())

print("\n===== SERVICE TYPE: RAW vs CANONICAL =====")
print(df[["service_type_raw", "service_type_canonical"]].drop_duplicates())

# ---------------- NUMERIC CONVERSION ---------------- #
numeric_cols = ["units_used", "provision_capacity", "availability", "cost_use",
                "external_holiday", "internal_maintenance"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop any rows that became NaN after conversion
df = df.dropna(subset=numeric_cols)

# Sort by timestamp
df = df.sort_values("timestamp")

# ---------------- PRINT DATASET INFO ---------------- #
print("\n===== DATASET COLUMNS =====")
print(df.columns)

print("\n===== FIRST 50 ROWS =====")
print(df.head(50))

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

# ---------------- GRAPHS ---------------- #

# 1️⃣ Units Used Over Time
plt.figure()
plt.plot(df["timestamp"], df["units_used"])
plt.title("Units Used Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Units Used")
plt.xticks(rotation=45)
plt.show()

# 2️⃣ Provision Capacity Over Time
plt.figure()
plt.plot(df["timestamp"], df["provision_capacity"])
plt.title("Provision Capacity Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Provision Capacity")
plt.xticks(rotation=45)
plt.show()

# 3️⃣ Usage vs Provision
plt.figure()
plt.scatter(df["provision_capacity"], df["units_used"])
plt.title("Usage vs Provision Capacity")
plt.xlabel("Provision Capacity")
plt.ylabel("Units Used")
plt.show()

# 4️⃣ Holiday Impact on Usage
plt.figure()
df.groupby("external_holiday")["units_used"].mean().plot(kind="bar")
plt.title("Holiday Impact on Usage")
plt.xlabel("External Holiday (0=No, 1=Yes)")
plt.ylabel("Average Units Used")
plt.show()

# 5️⃣ Internal Maintenance Impact on Availability
plt.figure()
df.groupby("internal_maintenance")["availability"].mean().plot(kind="bar")
plt.title("Maintenance Impact on Availability")
plt.xlabel("Internal Maintenance (0=No, 1=Yes)")
plt.ylabel("Average Availability")
plt.show()

# 6️⃣ Region-wise Usage (Canonical)
plt.figure()
df.groupby("region_canonical")["units_used"].mean().plot(kind="bar")
plt.title("Average Usage by Region")
plt.xlabel("Region")
plt.ylabel("Average Units Used")
plt.show()

# 7️⃣ Service Type Usage (Canonical)
plt.figure()
df.groupby("service_type_canonical")["units_used"].mean().plot(kind="bar")
plt.title("Average Usage by Service Type")
plt.xlabel("Service Type")
plt.ylabel("Average Units Used")
plt.show()

# 8️⃣ Usage Distribution
plt.figure()
plt.hist(df["units_used"], bins=15)
plt.title("Usage Distribution")
plt.xlabel("Units Used")
plt.ylabel("Frequency")
plt.show()

# 9️⃣ Provision Capacity Distribution
plt.figure()
plt.hist(df["provision_capacity"], bins=15)
plt.title("Provision Capacity Distribution")
plt.xlabel("Provision Capacity")
plt.ylabel("Frequency")
plt.show()
