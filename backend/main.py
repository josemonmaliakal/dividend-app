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
    results = []
    for row in rows:
        company = row[0]
        symbol = row[1]
        # Fetch historical dividends for this symbol (excluding the current month/year)
        # Get yearly total dividends for this symbol, excluding current month/year
        hist_query = '''
            SELECT strftime('%Y', ex_date) AS yr, SUM(dividend)
            FROM dividends
            WHERE symbol = ?
              AND NOT (strftime('%m', ex_date) = ? AND strftime('%Y', ex_date) = ?)
            GROUP BY yr
            ORDER BY yr ASC
            LIMIT 5
        '''
        cursor.execute(hist_query, (symbol, f"{month:02d}", str(year)))
        history_rows = cursor.fetchall()
        history = [
            {"year": hist_row[0], "dividend": hist_row[1]}
            for hist_row in history_rows
        ]
        results.append({
            "company": company,
            "symbol": symbol,
            "dividend": row[2],
            "ex_date": row[3],
            "record_date": row[4],
            "type": row[5],
            "history": history
        })

   

    conn.close()
    return results
