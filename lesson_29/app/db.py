import os
import psycopg2

def connect():
    host = os.getenv('DB_HOST', 'localhost')
    return psycopg2.connect(
        dbname="test_db",
        user="postgres",
        password="postgres",
        host=host,
        port=5432
    )

def init_db():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_user(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s);", (name,))
    conn.commit()
    cur.close()
    conn.close()

def update_user(user_id, new_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = %s WHERE id = %s;", (new_name, user_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_user(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

def get_users():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
