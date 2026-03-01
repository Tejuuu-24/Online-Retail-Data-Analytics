# ==========================================
# TASK 1: DATA UNDERSTANDING & DATA QUALITY
# Dataset: Online Retail
# ==========================================

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# 1. Load Dataset
# ------------------------------------------
df = pd.read_excel("C:/Users/DELL/Desktop/ApexPlanet-Data-Analytics-Internship/data/Online Retail Data Set.xlsx")

# ------------------------------------------
# 2. Initial Data Understanding
# ------------------------------------------
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())

print("\nFirst 5 Records:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe())

# ------------------------------------------
# 3. Data Quality Checks
# ------------------------------------------

# Missing values
print("\nMissing Values per Column:")
print(df.isnull().sum())

# Duplicate records
duplicate_count = df.duplicated().sum()
print("\nNumber of Duplicate Records:", duplicate_count)

# Check negative quantities
negative_qty = df[df['Quantity'] <= 0].shape[0]
print("\nRecords with Negative or Zero Quantity:", negative_qty)

# Cancelled invoices
cancelled_invoices = df[df['InvoiceNo'].astype(str).str.startswith('C')].shape[0]
print("Cancelled Transactions:", cancelled_invoices)

# ------------------------------------------
# 4. Data Cleaning Decisions
# ------------------------------------------

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Exclude cancelled invoices
df_cleaned = df_cleaned[~df_cleaned['InvoiceNo'].astype(str).str.startswith('C')]

# Exclude negative and zero quantities for revenue analysis
df_cleaned = df_cleaned[df_cleaned['Quantity'] > 0]

# Create TotalAmount column
df_cleaned['TotalAmount'] = df_cleaned['Quantity'] * df_cleaned['UnitPrice']

print("\nCleaned Dataset Shape:", df_cleaned.shape)

# ------------------------------------------
# 5. Exploratory Data Analysis (Basic)
# ------------------------------------------

# Revenue distribution
plt.hist(df_cleaned['TotalAmount'], bins=50)
plt.yscale('log')
plt.title("Distribution of Transaction Revenue (Log Scale)")
plt.xlabel("Total Amount")
plt.ylabel("Frequency (Log)")
plt.show()




# Quantity distribution
plt.figure()
sns.boxplot(x=df_cleaned['Quantity'])
plt.title("Boxplot of Quantity")
plt.show()

# Unit price distribution
plt.figure()
sns.boxplot(x=df_cleaned['UnitPrice'])
plt.title("Boxplot of Unit Price")
plt.show()

# Country-wise revenue (Top 10)
country_revenue = df_cleaned.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
country_revenue.plot(kind='bar')
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Total Revenue")
plt.show()

# ------------------------------------------
# 6. Final Output
# ------------------------------------------
print("\nFinal dataset is cleaned and ready for analysis.")

output_path = r"C:/Users/DELL/Desktop/ApexPlanet-Data-Analytics-Internship/data/cleaned_online_retail.csv"
df_cleaned.to_csv(output_path, index=False)
print("\nCleaned dataset saved to:")
print(output_path)

