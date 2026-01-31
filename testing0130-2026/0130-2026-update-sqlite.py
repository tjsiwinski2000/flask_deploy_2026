# INSERT OR REPLACE → safe to re-run without duplicates
# Explicit column list → future-proof
# Schema matches your JSON exactly
# SQLite-friendly, no ORM required

import sqlite3, json
from coffee_shops import shops

db_name = "coffee.db"
# cur = conn.cursor()

with sqlite3.connect(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coffee_shops (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            description TEXT,
            image_url TEXT
        )
    """)
    
    cursor.executemany(
        """
        INSERT OR REPLACE INTO coffee_shops
        (id, name, address, description, image_url)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (
                d["id"],
                d["name"],
                d["address"],
                d["description"],
                d["image_url"]
            )
            for d in shops
        ]
    )

