from .db import get_connection

def fetch_all_users():
    conn = get_connection()
    users = conn.execute('SELECT id, name FROM users').fetchall()
    conn.close()
    return [dict(u) for u in users]
