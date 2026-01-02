# Marketing Campaign Analysis – Rule-Based Customer Segmentation

## 📌 Project Overview
This project analyzes customer data from multiple marketing campaigns run by a retail company.  
The goal is to identify high-value customer segments, understand campaign response behavior, and derive actionable business insights using data analytics techniques.

The project covers:
- Data cleaning and feature engineering
- Exploratory Data Analysis (EDA)
- Rule-based customer segmentation
- SQL-based analytical queries
- An interactive Streamlit dashboard for business users

---

## 🧠 Business Problem
The management team wants to understand:
- Who are the most valuable customers?
- Which customer segments respond best to marketing campaigns?
- How spending and channel usage vary across different customer groups?
- Which customer profiles should be targeted in future campaigns?

---

## 🛠️ Tech Stack
- **Python**: Pandas, NumPy
- **EDA & Visualization**: Matplotlib, Seaborn
- **Dashboard**: Streamlit
- **Database & Queries**: SQL
- **Documentation**: Markdown, PDF

---

## 📂 Project Structure
marketing-campaign-analysis/
│
├── dashboard/
│ ├── app.py
│ └── final_marketing_data.csv
│
├── 01_data_cleaning.ipynb
├── 02_eda.ipynb
├── 03_segmentation.ipynb
│
├── sql/
│ ├── schema.sql
│ └── analysis_queries.sql
│
├── reports/
│ └── project_report.pdf
│
└── README.md


---

## 🔄 Workflow
1. **Data Cleaning**
   - Handled missing values
   - Converted data types
   - Created derived features such as Age, Total Spend, Children, and Total Purchases

2. **Exploratory Data Analysis**
   - Univariate and bivariate analysis
   - Spending patterns vs income and age
   - Campaign response behavior

3. **Rule-Based Segmentation**
   - High Income
   - High Spender
   - Young Customer
   - Family Customer
   - Campaign Responder
   - High Web Engagement

4. **SQL Analysis**
   - Table creation (DDL)
   - Analytical queries for KPIs and segment summaries

5. **Dashboard**
   - Interactive Streamlit app
   - Segment-based filtering
   - KPI cards and data preview

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install pandas numpy streamlit matplotlib seaborn

2️⃣ Run notebooks (in order)
jupyter notebook 01_data_cleaning.ipynb
jupyter notebook 02_eda.ipynb
jupyter notebook 03_segmentation.ipynb

3️⃣ Run Streamlit Dashboard
streamlit run dashboard/app.py
