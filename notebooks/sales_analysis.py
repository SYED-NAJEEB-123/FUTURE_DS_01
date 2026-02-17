import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/train.csv")

print("FIRST 5 ROWS")
print(df.head())

print("\nCOLUMNS:")
print(df.columns)

print("\nDATA INFO:")
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nSUMMARY:")
print(df.describe())


# ---------- DATA CLEANING ----------
df.drop_duplicates(inplace=True)

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])


# ---------- REVENUE TREND ----------
monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

plt.figure()
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("../images/monthly_sales.png")


# ---------- TOP PRODUCTS ----------
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure()
top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.ylabel("Revenue")
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig("../images/top_products.png")


# ---------- REGION PERFORMANCE ----------
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.ylabel("Revenue")
plt.savefig("../images/region_sales.png")

print("\nAnalysis Completed!")

