import sqlite3, json,os
# Lines below set path of database file to working path of program; prevents issues
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "coffee.db")

def get_coffee_shops(db_name=DB_PATH):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM coffee_shops")
        rows = cursor.fetchall()

        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in rows]
    
shops = get_coffee_shops()
print(shops)
print(type(shops))