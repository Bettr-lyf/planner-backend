import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']  # Use the environment variable provided by Replit

try:
    conn = psycopg2.connect(DATABASE_URL)  # This will use Replit's provided DATABASE_URL
    print("Connection successful.")
except Exception as e:
    print("Connection failed:", e)
finally:
    if 'conn' in locals():
        conn.close()