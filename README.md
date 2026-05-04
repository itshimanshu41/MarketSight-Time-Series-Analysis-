# 📊 MarketSight — SQL-Based Time Series Analysis

MarketSight is a Python-based data analysis project that uses SQL to extract insights from time-based sales data.

## 🚀 Features
- SQLite database integration  
- SQL queries (AVG, MAX, MIN)  
- High sales detection  
- CSV export  
- Clean modular structure  

## 🛠️ Tech Stack
- Python  
- SQLite  
- Pandas  

## 📁 Project Structure
marketsight/
│── data/
│   └── sales.db
│── src/
│   ├── setup_db.py
│   ├── queries.py
│   ├── analysis.py
│   └── main.py
│── output/
│   └── report.csv
│── requirements.txt
│── README.md

## ⚙️ How It Works
1. Creates SQLite database and inserts data  
2. Runs SQL queries (AVG, MAX, MIN)  
3. Detects high sales days  
4. Exports results to CSV  

## ▶️ How to Run
git clone https://github.com/itshimanshu41/MarketSight-Time-Series-Analysis-.git
cd MarketSight-Time-Series-Analysis-
pip install -r requirements.txt
cd src
python main.py

## 📊 Sample Output
Average: 118.0  
Max: 150  
Min: 90  

High Sales Days:  
('2024-01-04', 150)  
('2024-01-05', 130)  

CSV report generated!

## 🎯 Key Learnings
- SQL queries in Python  
- Data analysis using SQLite  
- CSV export using Pandas  

## 🚀 Future Improvements
- Add graphs  
- Use real dataset  
- Add dashboard  

## 👨‍💻 Author
Himanshu Mishra  
https://github.com/itshimanshu41
