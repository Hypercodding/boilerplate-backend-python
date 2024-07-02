import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Fetch database credentials from environment variables
DB_NAME = os.getenv("RAILWAY_DATABASE_NAME", "users")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("PGPASSWORD")
DB_HOST = os.getenv("PGHOST")
DB_PORT = os.getenv("PGPORT", "5432")  # Default port for PostgreSQL

# Establish database connection
conn = psycopg2.connect(
    dbname=DB_NAME,
    user="postgres",
    password=DB_PASSWORD,
    host="roundhouse.proxy.rlwy.net",
    port=DB_PORT,
    cursor_factory=RealDictCursor
)

# Creating a cursor object
cur = conn.cursor()
