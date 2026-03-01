DATA QUALITY REPORT - ONLINE RETAIL DATASET

1. DATASET OVERVIEW  
    Dataset Name: Online Retail Dataset  
    Source: Kaggle  
    Domain: Retail / E-commerce  
    Data Type: Transaction-level sales data

Objective:  
To assess data quality issues and prepare an analysis-ready dataset for accurate revenue, product performance, and sales trend analysis.

2. DATA QUALITY ISSUES IDENTIFIED

2.1 Missing Values  
Observation:  
CustomerID contains missing values in several records.

Impact:  
Missing CustomerID limits customer-level analysis but does not affect product-level sales or revenue calculations.

Action Taken:  
Rows with missing CustomerID were retained to avoid underreporting total sales and revenue.

2.2 Duplicate Records  
Observation:  
Duplicate transaction records were identified.

Impact:  
Duplicates can inflate revenue, sales quantity, and demand trends.

Action Taken:  
Duplicate rows were removed based on complete record matching to ensure accuracy.

2.3 Negative and Zero Quantities  
Observation:  
The Quantity column contains negative and zero values.

Interpretation:  
Negative quantities represent product returns or order cancellations.

Impact:  
Including these values in revenue calculations can distort net sales figures.

Action Taken:  
Negative and zero quantities were excluded from revenue calculations but retained for return and cancellation analysis.

2.4 Cancelled Transactions  
Observation:  
Invoice numbers starting with the letter "C" indicate cancelled transactions.

Impact:  
Cancelled invoices do not represent completed sales and can misrepresent revenue.

Action Taken:  
Cancelled transactions were excluded from net revenue analysis.

3. DERIVED COLUMN

TotalAmount  
Definition:  
TotalAmount = Quantity × UnitPrice

Purpose:  
Used as the primary metric for revenue, sales trend, and performance analysis.

4. DATA CLEANING SUMMARY

- Removed duplicate records to avoid double counting
- Retained missing CustomerID records for product and revenue analysis
- Excluded cancelled invoices and negative quantities from revenue calculations
- Created a TotalAmount column for accurate revenue measurement

5. FINAL DATA READINESS ASSESSMENT

The dataset is clean, consistent, and suitable for:

- Revenue analysis
- Product performance analysis
- Time-based sales trends
- Geographic sales insights

6. LIMITATIONS

- Customer-level analysis is partially limited due to missing CustomerID values
- Profit analysis is not possible due to absence of cost data

7. CONCLUSION

After performing data quality checks and cleaning actions, the dataset is analysis-ready and provides reliable insights for retail business decision-making.