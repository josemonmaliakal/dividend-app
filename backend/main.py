from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import sqlite3

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/dividends")
def get_dividends(month: int, year: int):
    conn = sqlite3.connect("data/dividends.db")
    cursor = conn.cursor()

    # Filter using SQLite strftime to extract year and month from ex_date
    query = '''
        SELECT company, symbol, dividend, ex_date, record_date, type
        FROM dividends
        WHERE strftime('%m', ex_date) = ? AND strftime('%Y', ex_date) = ?
    '''
    cursor.execute(query, (f"{month:02d}", str(year)))
    rows = cursor.fetchall()

    # Convert to dict list
    results = [
        {
            "company": row[0],
            "symbol": row[1],
            "dividend": row[2],
            "ex_date": row[3],
            "record_date": row[4],
            "type": row[5],
        }
        for row in rows
    ]

    conn.close()
    return results
