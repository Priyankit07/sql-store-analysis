# sql-store-analysis
MySQL + Python project analyzing store sales, customers, and performance
# Cycle Store Data Analysis (SQL + Python Project)

This project analyzes a fictional cycle store's data using **MySQL** and **Python**.  
It answers real business questions such as:  
- Which staff brings the most revenue?
- Who are the most loyal customers?
- Which product or store underperforms?

📊 This is a beginner-level but real-world inspired project that focuses on **query writing**, **data import automation**, and **business insights**.

---

## 📁 Project Structure
📦 sql-store-analysis/
├── first-sql-project.sql # SQL queries for analysis
├── load_data.py # Python script to load CSV files into MySQL
├── Screenshot_Archive.zip # Zipped version of all screenshots
└── .env (optional) # MySQL credentials (optional)

---

## 🧪 Tech Stack

- **Database:** MySQL 8.0
- **Languages:** SQL, Python
- **Libraries:** pandas, sqlalchemy, pymysql
- **Tools:** MySQL Workbench, VSCode

---

## ⚙️ How to Run This Project

> Note: The CSV file paths in `load_data.py` are hardcoded to a specific folder (`C:/Users/ADMIN/Downloads/archive (3)/`). You'll need to update these paths if you're replicating the project.

### Step 1: Create MySQL Database

Open MySQL Workbench or CLI and run:

```sql
CREATE DATABASE {give a name of your own suit};
```

### Step 2: Install Python Dependencies
```bash
pip install pandas sqlalchemy pymysql python-dotenv
```

### Step 3: Run the Python Script
```bash
python load_data.py
```

This will load 9 CSVs into MySQL tables.

Step 2: Install Python Dependencies
pip install pandas sqlalchemy pymysql python-dotenv

Step 3: Run the Python Script
python load_data.py
This will load 9 CSVs into MySQL table

📄 File: first-sql-project.sql

✅ Top 5 Most Sold Products

✅ Monthly Revenue Trends

✅ Revenue per Staff

✅ Most Loyal Customers

✅ Product Category with Most Revenue

✅ Highest Selling Product per Store

✅ Underperforming Stores

✅ Average Order Value per Customer

✅ Store-wise Product Revenue

✅ Staff Ranking by Sales

✅ And more...

Every screenshot filename corresponds to the query number in first-sql-project.sql.
download them all at once from Screenshot_Archive.zip.

📌 What I Learned
1. Writing real SQL queries using JOIN, GROUP BY, SUM, COUNT, etc.

2. Understanding business needs and translating them to data logic

3. Using Python to automate data loading into a SQL database

4. Structuring and sharing projects publicly

🙋‍♂️ About Me
I'm currently studying Computer Applications and working towards becoming a Data Scientist.
My focus is on practical learning through hands-on projects using Python, SQL, and real data.
