import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in preprocessed data
df = pd.read_csv("gold_data_preprocessed.csv")

# Convert 'Time' column to datetime format
df["Time"] = pd.to_datetime(df["Time"])

# Plot gold price over time
plt.figure(figsize=(12, 6))
sns.lineplot(x="Time", y="Gold_Price", data=df)
plt.title("Gold Price Over Time")
plt.xlabel("Time")
plt.ylabel("Gold Price (USD)")
plt.show()

# Plot correlation heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Plot gold price vs. economic indicators
economic_cols = ["CPI", "UNRATE", "FEDFUNDS", "GDP"]
for col in economic_cols:
    plt.figure(figsize=(12, 6))
    sns.regplot(x=col, y="Gold_Price", data=df)
    plt.title(f"Gold Price vs. {col}")
    plt.xlabel(col)
    plt.ylabel("Gold Price (USD)")
    plt.show()

# Plot gold price vs. stock market performance
stock_cols = ["SPY_Open", "SPY_Close"]
for col in stock_cols:
    plt.figure(figsize=(12, 6))
    sns.regplot(x=col, y="Gold_Price", data=df)
    plt.title(f"Gold Price vs. {col}")
    plt.xlabel(col)
    plt.ylabel("Gold Price (USD)")
    plt.show()

# Plot gold price vs. currency exchange rates
currency_cols = ["EUR_USD", "JPY_USD", "GBP_USD", "CAD_USD", "AUD_USD"]
for col in currency_cols:
    plt.figure(figsize=(12, 6))
    sns.regplot(x=col, y="Gold_Price", data=df)
    plt.title(f"Gold Price vs. {col}")
    plt.xlabel(col)
    plt.ylabel("Gold Price (USD)")
    plt.show()

# Plot gold price vs. demand for gold
demand_cols = ["Jewelry_Demand", "Technology_Demand", "Investment_Demand"]
for col in demand_cols:
    plt.figure(figsize=(12, 6))
    sns.regplot(x=col, y="Gold_Price", data=df)
    plt.title(f"Gold Price vs. {col}")
    plt.xlabel(col)
    plt.ylabel("Gold Price (USD)")
    plt.show()

# Plot gold price vs. supply of gold
supply_cols = ["Gold_Production", "Gold_Supply"]
for col in supply_cols:
    plt.figure(figsize=(12, 6))
    sns.regplot(x=col, y="Gold_Price", data=df)
    plt.title(f"Gold Price vs. {col}")
    plt.xlabel(col)
    plt.ylabel("Gold Price (USD)")
    plt.show()

# Plot gold price vs. geopolitical events
event_cols = ["War", "Political_Instability", "Trade_Tensions"]
for col in event_cols:
    plt.figure(figsize=(12, 6))
    sns.regplot(x=col, y="Gold_Price", data=df)
    plt.title(f"Gold Price vs. {col}")
    plt.xlabel(col)
    plt.ylabel("Gold Price (USD)")
    plt.show()
