

# ==========================================
# TASK 2: EXPLORATORY DATA ANALYSIS (EDA)
# Dataset: Cleaned Online Retail Data
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# ------------------------------------------
# 1. Load CLEANED dataset
# ------------------------------------------
df = pd.read_csv(
    "C:/Users/DELL/Desktop/ApexPlanet-Data-Analytics-Internship/data/cleaned_online_retail.csv"
)

print("Dataset Shape:", df.shape)
print(df.info())
print(df.head())

# ------------------------------------------
# 2. Revenue Distribution
# ------------------------------------------
save_dir = r"C:\Users\DELL\Desktop\ApexPlanet-Data-Analytics-Internship\visuals"
os.makedirs(save_dir, exist_ok=True)

plt.figure(figsize=(8,5))
plt.hist(df['TotalAmount'], bins=5)
plt.yscale('log')
plt.title("Distribution of Transaction Revenue (Log Scale)")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")

plt.savefig(
    os.path.join(save_dir, "revenue_distribution_log.png"),
    bbox_inches="tight"
)

plt.show()
plt.close()


# ------------------------------------------
# 3. Monthly Revenue Trend
# ------------------------------------------
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M')

monthly_revenue = df.groupby('YearMonth')['TotalAmount'].sum()

save_dir = r"C:\Users\DELL\Desktop\ApexPlanet-Data-Analytics-Internship\visuals"
os.makedirs(save_dir, exist_ok=True)
plt.figure(figsize=(12,5))
monthly_revenue.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)

plt.savefig(
    os.path.join(save_dir, "Monthly_Revenue_Trend.png"),
    bbox_inches="tight"
)

plt.show()
plt.close()
# ------------------------------------------
# 4. Top 10 Products by Revenue
# ------------------------------------------
top_products = (
    df.groupby('Description')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
save_dir = r"C:\Users\DELL\Desktop\ApexPlanet-Data-Analytics-Internship\visuals"
os.makedirs(save_dir, exist_ok=True)

plt.figure(figsize=(10,5))
top_products.plot(kind='bar')
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.savefig(
    os.path.join(save_dir, "Monthly_Revenue_Trend.png"),
    bbox_inches="tight"
)

plt.show()
plt.close()

# ------------------------------------------
# 5. Top 10 Countries by Revenue
# ------------------------------------------
top_countries = (
    df.groupby('Country')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
save_dir = r"C:\Users\DELL\Desktop\ApexPlanet-Data-Analytics-Internship\visuals"
os.makedirs(save_dir, exist_ok=True)


plt.figure(figsize=(5,5))
top_countries.plot(kind='bar')
plt.title("Top 5 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.savefig(
    os.path.join(save_dir, "top_5_countries.png"),
    bbox_inches="tight"
)

plt.show()
plt.close()
# ------------------------------------------
# 6. Top 10 Customers by Revenue
# ------------------------------------------
top_customers = (
    df.groupby('CustomerID')['TotalAmount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Revenue:")
print(top_customers)

# ------------------------------------------
# END OF TASK 2
# ------------------------------------------
print("\nTask 2 EDA completed successfully.")
