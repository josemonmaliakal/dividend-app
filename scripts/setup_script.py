import sqlite3
import json

# Load mock JSON
with open("../backend/data/mock_dividends.json") as f:
    dividend_data = json.load(f)

# Create DB and table
conn = sqlite3.connect("dividends.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS dividends (
    company TEXT,
    symbol TEXT,
    dividend REAL,
    ex_date TEXT,
    record_date TEXT,
    type TEXT
)
''')

# Optional: Clear existing entries for repeatable runs
cursor.execute("DELETE FROM dividends")

# Insert data
for item in dividend_data:
    cursor.execute('''
        INSERT INTO dividends (company, symbol, dividend, ex_date, record_date, type)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (item['company'], item['symbol'], item['dividend'], item['ex_date'], item['record_date'], item['type']))

conn.commit()
conn.close()
