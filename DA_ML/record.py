
import numpy as np
import pandas as pd

np.random.seed(42)

# Generate 1000 Normal records
normal = pd.DataFrame({
    "MQ2": np.random.uniform(0, 17.1, 1000),
    "TEMP": np.random.uniform(18, 35, 1000),
    "HUMIDITY": np.random.uniform(25, 85, 1000),
    "Normal_Flag": 1,
    "Warning_Flag": 0,
    "Critical_Flag": 0
})

# Generate 1000 Warning records
warning = pd.DataFrame({
    "MQ2": np.random.uniform(17.1001, 25.5, 1000),
    "TEMP": np.random.uniform(18, 35, 1000),
    "HUMIDITY": np.random.uniform(25, 85, 1000),
    "Normal_Flag": 0,
    "Warning_Flag": 1,
    "Critical_Flag": 0
})

# Generate 1000 Critical records
critical = pd.DataFrame({
    "MQ2": np.random.uniform(25.5001, 1000, 1000),
    "TEMP": np.random.uniform(18, 35, 1000),
    "HUMIDITY": np.random.uniform(25, 85, 1000),
    "Normal_Flag": 0,
    "Warning_Flag": 0,
    "Critical_Flag": 1
})

# Combine all datasets
df = pd.concat(
    [normal, warning, critical],
    ignore_index=True
)

# Shuffle records
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Round sensor readings
df["MQ2"] = df["MQ2"].round(2)
df["TEMP"] = df["TEMP"].round(2)
df["HUMIDITY"] = df["HUMIDITY"].round(2)

# Save to CSV
df.to_csv("balanced_mq2_dataset.csv", index=False)

# Display results
print("Dataset generated successfully!")
print("Total records:", len(df))

print("\nClass distribution:")
print(df[["Normal_Flag", "Warning_Flag", "Critical_Flag"]].sum())

print("\nFirst 10 records:")
print(df.head(10))

print("\nCSV saved as balanced_mq2_dataset.csv")
