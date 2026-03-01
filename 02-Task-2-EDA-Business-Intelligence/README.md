Task 2: Exploratory Data Analysis & Business Intelligence 

📌 Objective
The objective of Task 2 is to perform **Exploratory Data Analysis (EDA)** and **Business Intelligence analysis** on the cleaned Online Retail dataset to extract meaningful insights related to revenue, transactions, products, customers, and time-based trends.  
This task focuses on understanding business performance through data visualization and analytical reasoning.

📊 Dataset
- Source: Online Retail Dataset  
- Type: Transactional retail data  
- Time Period: December 2010 – December 2011  
- Data Used: Cleaned dataset obtained from Task 1  

The cleaned dataset contains only valid transactions with:
- No cancelled invoices
- No negative or zero quantities
- Duplicate records removed
- Derived revenue column (`TotalAmount`)

🛠 Tools & Technologies Used
- Python - (Pandas, Matplotlib, Seaborn) – EDA & preprocessing
- SQL – Business metric validation
- Power BI – Interactive dashboard & visualization

🔍 Exploratory Data Analysis (EDA)
The following analyses were performed:
- Revenue distribution analysis
- Monthly revenue trend analysis
- Top products by revenue
- Revenue contribution by country.
  
EDA helped in identifying:
- Seasonal sales patterns
- Revenue concentration across products and countries.
  
🧮 SQL Analysis
SQL queries were written to **validate and calculate business metrics** before visualization.  
The queries include:

- Total Revenue
- Total Number of Transactions
- Average Order Value
- Monthly Revenue Trend
- Top Products by Revenue
- Revenue by Country
- Top Customers by Revenue  

📁 SQL queries are available in: sql/sql_queries.sql

 📈 Dashboard (Power BI)
An interactive Power BI dashboard was created to visualize insights, including:
 Key KPIs :
- Total Revenue
- Total Transactions
- Average Order Value
 Visualizations:
- Monthly Revenue Trend (Year–Month)
- Top 5 Products by Revenue
- Revenue Contribution by Country
The dashboard provides a clear and business-friendly overview of sales performance.

📁 Project Structure:
Task-2-EDA-Business-Intelligence/
│
├── data/
│ └── cleaned_online_retail.csv
│
├── code/
│ └── task2.py
│
├── sql/
│ └── sql_queries.sql
│
├── visuals/
│ └── images
├── dashboard/
│ └── powerbi_dashboard.pbix
│
└── README.md

Key Insights:
- Revenue shows steady growth through 2011 with a peak in November.
- The United Kingdom contributes the highest share of total revenue.
- A small number of products generate a large portion of revenue.
- December 2011 shows lower revenue due to partial month data.

Conclusion:
Task 2 demonstrates the ability to analyze retail data, validate metrics using SQL, and communicate insights through effective visualizations using Power BI.

