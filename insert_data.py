import os
import pandas as pd
import psycopg2
from psycopg2 import sql
from flood_validation import validate_csv

# Database connection details
DB_NAME = "flood_data"
DB_USER = "flood_user"
DB_PASSWORD = "your_secure_password"
DB_HOST = "localhost"
DB_PORT = "5432"

# File paths
DATA_DIR = "/home/ubuntu/data"
TABLE_MAPPINGS = {
    "noaa_water_levels": ["timestamp", "water_level_m"],
    "usgs_water_levels": ["timestamp", "water_level_m"],
    "twitter_flood_reports": ["tweet_id", "timestamp", "lat", "lon", "flood_severity"],
    "gis_flood_zones": ["zone_id", "timestamp", "lat", "lon", "flood_risk_level"]
}

def connect_db():
    """Establishes a connection to the PostgreSQL database."""
    try:
        return psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
    except psycopg2.Error as e:
        print(f"❌ Database connection error: {e}")
        return None

def process_csv(file_path, table_name):
    """Validates CSV data and inserts it into the appropriate database table."""
    print(f"📄 Processing: {file_path}")
    
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print(f"⚠️ Skipping {file_path}: CSV is completely empty.")
        return
    
    df = pd.read_csv(file_path)
    
    if df.empty:
        print(f"⚠️ Skipping {file_path}: No valid data found (EmptyDataError).")
        return

    df = validate_csv(df, table_name)  # Ensure valid columns
    
    if df is None or df.empty:
        print(f"⚠️ No valid data in {file_path}. Skipping.")
        return
    
    conn = connect_db()
    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            columns = TABLE_MAPPINGS.get(table_name, [])
            if not columns:
                print(f"⚠️ No table mapping found for {file_path}. Skipping.")
                return

            query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
                sql.Identifier(table_name),
                sql.SQL(', ').join(map(sql.Identifier, columns)),
                sql.SQL(', ').join(sql.Placeholder() * len(columns))
            )

            for _, row in df.iterrows():
                cur.execute(query, tuple(row[col] for col in columns))

            conn.commit()
            print(f"✅ Successfully inserted data into {table_name}")
    except psycopg2.Error as e:
        print(f"❌ Error processing {file_path}: {e}")
    finally:
        conn.close()

def main():
    """Runs the data processing script for each expected CSV file."""
    for table_name in TABLE_MAPPINGS.keys():
        file_path = os.path.join(DATA_DIR, f"{table_name}_2025-02-28.csv")
        process_csv(file_path, table_name)

if __name__ == "__main__":
    main()
