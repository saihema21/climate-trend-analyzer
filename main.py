import pandas as pd
import os
import matplotlib.pyplot as plt

# Ensure folder exists
os.makedirs("data/processed", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/climate_data.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

print("Raw Data:\n", df.head())

# Save cleaned data
df.to_csv("data/processed/cleaned_data.csv", index=False)

# 📊 Plot 1: Temperature Trend
plt.figure()
plt.plot(df['Date'], df['Temperature'])
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("outputs/temperature_trend.png")

# 📊 Plot 2: Rainfall Trend
plt.figure()
plt.plot(df['Date'], df['Rainfall'])
plt.title("Rainfall Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Rainfall")
plt.savefig("outputs/rainfall_trend.png")

# 📊 Plot 3: CO2 Levels
plt.figure()
plt.plot(df['Date'], df['CO2'])
plt.title("CO2 Levels Over Time")
plt.xlabel("Date")
plt.ylabel("CO2")
plt.savefig("outputs/co2_trend.png")

print("✅ Graphs generated and saved in outputs folder!")
# 📊 Insights
print("\n📊 Climate Insights:")

print(f"🌡️ Average Temperature: {df['Temperature'].mean():.2f}")
print(f"🌧️ Total Rainfall: {df['Rainfall'].sum()}")
print(f"🌍 Average CO2 Level: {df['CO2'].mean():.2f}")

# Trend observation
if df['Temperature'].iloc[-1] > df['Temperature'].iloc[0]:
    print("📈 Temperature is increasing over time")

if df['CO2'].iloc[-1] > df['CO2'].iloc[0]:
    print("📈 CO2 levels are rising")