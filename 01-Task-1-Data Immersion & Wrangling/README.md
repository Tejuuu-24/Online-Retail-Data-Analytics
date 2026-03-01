ApexPlanet Data Analytics Internship
✅ Task 1: Data Immersion & Wrangling

This repository contains the completed work for Task 1 of the Data Analytics Internship at ApexPlanet Software Pvt. Ltd.
The objective of this task was to understand the dataset, assess data quality issues, apply business-driven cleaning logic, and prepare an analysis-ready dataset.

📁 Repository Structure
ApexPlanet-Data-Analytics-Internship
│
├── data/
│   ├── Online Retail Dataset.xlsx
│   └── cleaned_online_retail.xlsx
│
├── code/
│   └── task1program.py
│
├── DATA_QUALITY_REPORT.md
├── Data_Dictionary_Online_Retail.xlsx
└── README.md

📊 Dataset Information

Dataset Name: Online Retail Dataset
Source: Kaggle
Domain: Retail / E-commerce
Granularity: Transaction-level sales data


📘 Task 1 Work Summary

Data Understanding:
Reviewed dataset structure, columns, and data types
Analyzed transaction-level sales records


Data Quality Assessment:
Identified missing CustomerID values
Detected duplicate records
Identified cancelled invoices and return transactions


Data Cleaning Decisions:
Removed duplicate records to avoid double counting
Excluded cancelled invoices from revenue analysis
Excluded negative and zero quantities (returns)
Retained records with missing CustomerID for product-level analysis
Created a derived column:
TotalAmount = Quantity × UnitPrice


Exploratory Analysis:
Analyzed transaction revenue distribution
Identified highly right-skewed revenue behavior
Performed basic country-level revenue analysis


🎯 Outcome of Task 1
Produced a cleaned, analysis-ready dataset
Ensured accurate representation of revenue and sales trends
Established a reliable foundation for further analysis and modeling


🚀 Next Steps
Perform advanced exploratory analysis
Conduct customer and product-level insights
Build analytical models in subsequent tasks

🧑‍💼 Intern Details

Name: Tejaswini Sanam
Role: Data Analytics Intern
Organization: ApexPlanet Software Pvt. Ltd.

📌 Note
This repository will be updated as additional internship tasks are completed.

