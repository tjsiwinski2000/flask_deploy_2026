import sqlite3
import os

def test_setup():
    db_name = 'test_check.db'
    
    try:
        # Connect and create a table
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS status (msg TEXT)")
            cursor.execute("INSERT INTO status (msg) VALUES ('SQLite is working!')")
            
            # Retrieve the data
            cursor.execute("SELECT msg FROM status")
            result = cursor.fetchone()[0]
            
            print(f"✅ Success: {result}")
            print(f"📂 Database file created at: {os.path.abspath(db_name)}")
            
    except sqlite3.Error as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    test_setup()