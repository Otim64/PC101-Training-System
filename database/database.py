import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DB_PATH = os.path.join(PROJECT_DIR, "students.db")

print("=" * 60)
print("DATABASE PATH:", DB_PATH)
print("DATABASE EXISTS:", os.path.exists(DB_PATH))
print("=" * 60)


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn