import sqlite3
import json
import re
from datetime import datetime

# Load JSON from file
with open('data.json', 'r') as f:
    json_data = json.load(f)

# Connect to SQLite
conn = sqlite3.connect('dividends.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS dividends (
    company TEXT,
    symbol TEXT,
    dividend REAL,
    ex_date TEXT,
    record_date TEXT,
    type TEXT,
    UNIQUE(symbol, ex_date, type)
)
''')

# Helper to parse dividend info
def parse_dividend_subject(subject):
    entries = []
    patterns = {
        "Interim": r"interim dividend\s*-\s*rs\s*([\d.]+)",
        "Special": r"special dividend\s*-\s*rs\s*([\d.]+)",
        "Final": r"(?<!interim\s)(?<!special\s)dividend\s*-\s*rs\s*([\d.]+)"
    }
    for dtype, pattern in patterns.items():
        matches = re.findall(pattern, subject, re.IGNORECASE)
        for match in matches:
            try:
                amount = float(match)
                entries.append((dtype, amount))
            except ValueError:
                pass
    return entries

# Insert into DB
for entry in json_data:
    company = entry.get('comp')
    symbol = entry.get('symbol')
    ex_date = datetime.strptime(entry.get('exDate'), '%d-%b-%Y').strftime('%Y-%m-%d')
    if entry.get('recDate') != '-':
        record_date = datetime.strptime(entry.get('recDate'), '%d-%b-%Y').strftime('%Y-%m-%d')  
    subject = entry.get('subject', '')

    parsed_entries = parse_dividend_subject(subject)
    
    for dtype, dividend in parsed_entries:
        try:
            cursor.execute('''
            INSERT OR IGNORE INTO dividends (company, symbol, dividend, ex_date, record_date, type)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (company, symbol, dividend, ex_date, record_date, dtype))
        except Exception as e:
            print(f"Error inserting {symbol} ({dtype}): {e}")

# Commit and close
conn.commit()
conn.close()

print("Dividend data parsed and inserted successfully.")
