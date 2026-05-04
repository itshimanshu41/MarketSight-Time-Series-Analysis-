import sqlite3
import pandas as pd

def export_csv():
    conn = sqlite3.connect("../data/sales.db")
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()

    df.to_csv("../output/report.csv", index=False)
