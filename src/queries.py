import sqlite3

def get_summary():
    conn = sqlite3.connect("../data/sales.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT AVG(value), MAX(value), MIN(value)
    FROM sales
    """)

    result = cursor.fetchone()
    conn.close()
    return result


def get_high_sales():
    conn = sqlite3.connect("../data/sales.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT date, value
    FROM sales
    WHERE value > 120
    """)

    result = cursor.fetchall()
    conn.close()
    return result
