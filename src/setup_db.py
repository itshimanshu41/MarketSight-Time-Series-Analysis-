import sqlite3

def create_db():
    conn = sqlite3.connect("../data/sales.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        date TEXT,
        value INTEGER
    )
    """)

    # sample data
    data = [
        ("2024-01-01", 100),
        ("2024-01-02", 120),
        ("2024-01-03", 90),
        ("2024-01-04", 150),
        ("2024-01-05", 130)
    ]

    cursor.executemany("INSERT INTO sales VALUES (?, ?)", data)

    conn.commit()
    conn.close()
