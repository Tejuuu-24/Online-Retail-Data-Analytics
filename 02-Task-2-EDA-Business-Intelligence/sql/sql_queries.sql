/* =====================================================
   SQL ANALYSIS – ONLINE RETAIL DATASET
   Purpose: Business Intelligence & EDA Validation
   ===================================================== */

1. Total Revenue
-- Calculates overall revenue from all completed transactions
SELECT 
    SUM(Quantity * UnitPrice) AS Total_Revenue
FROM online_retail;


2. Total Number of Transactions
-- Counts unique invoices to represent total transactions
SELECT 
    COUNT(DISTINCT InvoiceNo) AS Total_Transactions
FROM online_retail;


3. Average Order Value (AOV)
-- Calculates average revenue per transaction
SELECT 
    SUM(Quantity * UnitPrice) / COUNT(DISTINCT InvoiceNo) AS Average_Order_Value
FROM online_retail;


4. Monthly Revenue Trend (Dec 2010 – Dec 2011)
-- Aggregates revenue by year and month to analyze trends
SELECT 
    YEAR(InvoiceDate) AS Year,
    MONTH(InvoiceDate) AS Month,
    SUM(Quantity * UnitPrice) AS Monthly_Revenue
FROM online_retail
GROUP BY Year, Month
ORDER BY Year, Month;


5. Top 5 Products by Revenue
-- Identifies highest revenue-generating products
SELECT 
    Description AS Product_Name,
    SUM(Quantity * UnitPrice) AS Product_Revenue
FROM online_retail
GROUP BY Description
ORDER BY Product_Revenue DESC
LIMIT 5;


6. Revenue Contribution by Country
-- Shows which countries contribute most to revenue
SELECT 
    Country,
    SUM(Quantity * UnitPrice) AS Country_Revenue
FROM online_retail
GROUP BY Country
ORDER BY Country_Revenue DESC;


7. Top 5 Customers by Revenue
-- Identifies high-value customers
SELECT 
    CustomerID,
    SUM(Quantity * UnitPrice) AS Customer_Revenue
FROM online_retail
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY Customer_Revenue DESC
LIMIT 5;
