import pandas as pd

TABLE_MAPPINGS = {
    "noaa_water_levels": ["timestamp", "water_level_m"],
    "usgs_water_levels": ["timestamp", "water_level_m"],
    "twitter_flood_reports": ["tweet_id", "timestamp", "lat", "lon", "flood_severity"],
    "gis_flood_zones": ["zone_id", "timestamp", "lat", "lon", "flood_risk_level"]
}

def validate_csv(df, table_name):
    """Ensures the CSV contains the required columns for the specified table."""
    required_columns = TABLE_MAPPINGS.get(table_name, [])
    
    if not required_columns:
        print(f"⚠️ No table mapping found for {table_name}. Skipping validation.")
        return None
    
    missing_cols = [col for col in required_columns if col not in df.columns]
    
    if missing_cols:
        print(f"❌ Missing columns {missing_cols} in {table_name}. Skipping file.")
        return None

    return df[required_columns]  # Return only necessary columns
