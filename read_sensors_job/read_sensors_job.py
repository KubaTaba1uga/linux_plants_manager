import datetime
import sqlite3

db_path = "/opt/sensors.db"

# Define file paths for sensor data
soil_humid_path = "/proc/soil_humid"
air_humid_path = "/proc/air_humid"
air_temp_path = "/proc/air_temp"


def read_sensor_value(file_path):
    """Read and return the sensor value from a given file as an integer."""
    try:
        with open(file_path, "r") as f:
            # Read, strip whitespace, and convert to integer
            return int(float(f.read().strip()))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


# Read sensor values from the files
soil_humid = read_sensor_value(soil_humid_path)
air_humid = read_sensor_value(air_humid_path)
air_temp = read_sensor_value(air_temp_path)

# Ensure all values were successfully read before proceeding
if None in (soil_humid, air_humid, air_temp):
    print("One or more sensor values could not be read. Exiting.")
    exit(1)

# Generate a timestamp for the record
timestamp = datetime.datetime.now().isoformat()

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table if it doesn't exist with integer columns for sensor readings
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS sensor_data (
        timestamp TEXT,
        soil_humid INTEGER,
        air_humid INTEGER,
        air_temp INTEGER
    )
"""
)
conn.commit()

# Insert the sensor data into the table
cursor.execute(
    "INSERT INTO sensor_data VALUES (?, ?, ?, ?)",
    (timestamp, soil_humid, air_humid, air_temp),
)
conn.commit()

conn.close()

print(
    f"{soil_humid_path}:{soil_humid}",
    f"{air_humid_path}:{air_humid}",
    f"{air_temp_path}:{air_temp}",
)
