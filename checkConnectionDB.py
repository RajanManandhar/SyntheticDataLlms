import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()


try:
    connection = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    cursor.execute("SELECT 1;")
    print("Connected to the database successfully!")
except Exception as e:
    print(f"Error connecting to the database: {e}")
finally:
    cursor.close()
    connection.close()
