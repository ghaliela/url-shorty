import os
import psycopg2
import dotenv

# Load environment variables
dotenv.load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")

# Connect to your postgres DB
conn = psycopg2.connect(f"dbname={db_name} user={db_user} password={db_password} host={db_host}")

# Open a cursor to perform database operations
cur = conn.cursor()

# initialize the database
existing_table = cur.execute("select * from information_schema.tables where table_name=%s", ('shorturls',))
if not bool(cur.rowcount):
    cur.execute("ROLLBACK;")
    cur.execute("BEGIN;")
    cur.execute("CREATE TABLE shortUrls ( id SERIAL PRIMARY KEY, short_hash VARCHAR(255) NOT NULL, long_url TEXT NOT NULL, clickCount int DEFAULT 0, UNIQUE(short_hash), UNIQUE(long_url) )")
    cur.execute("CREATE UNIQUE INDEX idx_short_url ON shortUrls (short_hash);")
    cur.execute("CREATE UNIQUE INDEX idx_long_url ON shortUrls (long_url);")
    cur.execute("COMMIT;")

cur.close()