# previous imports
import os
import psycopg2
import dotenv

# previous codes ...

dotenv.load_dotenv("../.env")

driver = psycopg2

def connect_to_database():
    return driver.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

connect_to_database()