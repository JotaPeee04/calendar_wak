import sqlite3, os
import datetime as dt
from src.models.event import event

def init_db():
    if not os.path.isdir("data"):
        os.mkdir("data")
    conn = sqlite3.connect('data/eventos.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, title varchar(255), description TEXT, s_date TEXT, " \
    "e_date TEXT, s_time TEXT, e_time TEXT, category_id INTEGER )")
    conn.commit()
    conn.close()

def insert_event(event):
    
    query = f"INSERT INTO events (title, description, s_date, e_date, s_time, e_time, category_id) VALUES ( ?, ?, ?, ?, ?, ?, ? )" 
    
    conn = sqlite3.connect('data/eventos.db')
    cursor = conn.cursor()
    cursor.execute(query, (event.title, event.description, event.s_date.isoformat(), event.e_date.isoformat(), event.s_time.isoformat(), event.e_time.isoformat(), event.category_id))
    event.id = cursor.lastrowid
    conn.commit()
    conn.close()

def fetch_events(selected_date=None) -> list:
    conn = sqlite3.connect('data/eventos.db')
    cursor = conn.cursor()
    if selected_date:
        cursor.execute("SELECT * FROM events WHERE s_date=?",(selected_date.isoformat(),))
    else:

        cursor.execute("SELECT * FROM events")
    fetched = cursor.fetchall()
    ls = []
    for e in fetched:
        ev = event(title=e[1], s_date=dt.date.fromisoformat(e[3]), e_date=dt.date.fromisoformat(e[4]), s_time=dt.time.fromisoformat(e[5]),e_time=dt.time.fromisoformat(e[6]),id=e[0],description=e[2],category_id=e[7])
        ls.append(ev)
    conn.close()
    return ls



def update_event(event):
    conn = sqlite3.connect('data/eventos.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE events SET title=?,description=?, s_date=?, e_date=?, s_time=?, e_time=?, category_id=?  WHERE id = ? ", 
                    (event.title, event.description, event.s_date.isoformat(), event.e_date.isoformat(), event.s_time.isoformat(), event.e_time.isoformat(), event.category_id, event.id))
    conn.commit()
    conn.close()

def delete_event(event_id : int):
    conn = sqlite3.connect('data/eventos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM events WHERE id=?",(event_id,))
    conn.commit()
    conn.close()


