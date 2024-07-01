import psycopg2
from psycopg2.extras import RealDictCursor

DB_NAME = "figma"
DB_USER = "postgres"
DB_PASSWORD = "Hyper"
DB_HOST = "localhost"


conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    cursor_factory=RealDictCursor
)

# Creating a cursor object
cur = conn.cursor()
