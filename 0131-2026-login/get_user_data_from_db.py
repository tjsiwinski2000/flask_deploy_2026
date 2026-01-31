import sqlite3, json,os
users={
    "tjsiwinski": {
        "password" : "foofoo1965",
        "email" : "foo@foo.com",
        "last login" :"2026-01-31"
    },
    "summersiwinski": {
        "password" : "foofoo2000",
        "email" : "foo@foo.com",
        "last login" :"2026-01-31"
    }
}

# below is temporary for pilot testing
def get_user_data_file(filter='all'):
    user_password ="not-found"
    for user_name,user_info in users.items():
        if user_name == filter:
            user_password = user_info['password']
    return user_password
    

#0131-2026 Below is for Phase2 when we use sqlite
# Lines below set path of database file to working path of program; prevents issues
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "user_data.db")

def get_user_data_db(db_name=DB_PATH,filter='all'):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()

        if filter == 'all':
             cursor.execute("SELECT * FROM users")
        else:
            cursor.execute("SELECT * FROM users where user_id =",(filter,))
        rows = cursor.fetchall()

        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in rows]
    
