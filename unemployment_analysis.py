import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
import pandas as pd

df = pd.read_csv(r"C:\Users\Arvind\Downloads\Unemployment in India.csv")

print(df.head())
print(df.columns.tolist())

# Display first rows
print("First 5 Records:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Rename columns (remove extra spaces)
df.columns = df.columns.str.strip()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Basic Statistics
print("\nStatistical Summary:")
print(df.describe())

# Average unemployment rate
avg_rate = df['Estimated Unemployment Rate (%)'].mean()
print(f"\nAverage Unemployment Rate: {avg_rate:.2f}%")

# -----------------------------
# Visualization 1
# -----------------------------
plt.figure(figsize=(12,6))
sns.lineplot(
    data=df,
    x='Date',
    y='Estimated Unemployment Rate (%)'
)

plt.title("Unemployment Rate Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Visualization 2
# -----------------------------
plt.figure(figsize=(12,6))
sns.barplot(
    data=df,
    x='Region',
    y='Estimated Unemployment Rate (%)'
)

plt.xticks(rotation=90)
plt.title("Region-wise Unemployment Rate")
plt.tight_layout()
plt.show()

# -----------------------------
# Covid Impact Analysis
# -----------------------------
covid_period = df[df['Date'] >= '2020-03-01']

plt.figure(figsize=(12,6))
sns.lineplot(
    data=covid_period,
    x='Date',
    y='Estimated Unemployment Rate (%)'
)

plt.title("Unemployment During COVID-19")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()