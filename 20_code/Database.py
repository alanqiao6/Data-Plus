import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import re

# Configuration
database_name = "ignite_database"
config = { 
    'user': "ignite",
    'password': 'ignite', 
    'host': 'localhost',
    'raise_on_warnings': True
}

# Connect to MySQL server (without specifying database)
conn = mysql.connector.connect(user=config['user'], password=config['password'], host=config['host'], raise_on_warnings=config['raise_on_warnings'])
cursor = conn.cursor()
table_names=['learners', 
             'makers',
             #'trainers'
             ]
# CHANGE FILE PATHS
csv_file_paths = [
                  "C:\\Users\\maris\\OneDrive - Duke University\\Desktop\\Data+\\GUI\\Learners_Database.csv", 
                  "C:\\Users\\maris\\OneDrive - Duke University\\Desktop\\Data+\\GUI\\Makers_Database.csv",
                  #"C:\\Users\\maris\\OneDrive - Duke University\\Desktop\\Data+\\GUI\\Trainers_Database.csv"
                  ]

 # Function to check if a database exists
def check_database_exists(cursor, database_name):
    cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
    result = cursor.fetchone()
    return result is not None

# Check if the database exists, if not create it
if not check_database_exists(cursor, database_name):
    cursor.execute(f"CREATE DATABASE {database_name}")
    print(f"Database '{database_name}' created successfully.")

for i in range(len(table_names)):
    table_name=table_names[i]
    csv_file_path=csv_file_paths[i]
    # Function to check if a table exists
    def check_table_exists(cursor, table_name):
        cursor.execute("SHOW TABLES LIKE %s", (table_name,))
        result = cursor.fetchone()
        return result is not None


    # Reconnect to the MySQL server with the new database
    conn.close()
    config['database'] = database_name
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Load CSV file
    df = pd.read_csv(csv_file_path)

    # Clean column names to be SQL-friendly and unique
    def clean_column_name(name, existing_names):
        name = re.sub(r'[^0-9a-zA-Z_]', '', name)  # Remove non-alphanumeric characters except underscores
        name = name[:60]  # Truncate to ensure there's room for a suffix
        new_name = name
        count = 1
        while new_name in existing_names:
            new_name = f"{name}_{count}"
            if len(new_name) > 64:  # Ensure the new name does not exceed 64 characters
                new_name = new_name[:64 - len(str(count)) - 1] + f"_{count}"
            count += 1
        existing_names.add(new_name)
        return new_name

    existing_names = set()
    df.columns = [clean_column_name(col, existing_names) for col in df.columns]

    # Replace NaN values with None
    df = df.where(pd.notnull(df), 'None')
    df.replace(r'^\s+$', 'None', regex=True)

    # Generate a CREATE TABLE statement based on the DataFrame columns
    def generate_create_table_sql(table_name, df):
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for col in df.columns:
            if pd.api.types.is_integer_dtype(df[col]):
                sql += f"{col} INT, "
            elif pd.api.types.is_float_dtype(df[col]):
                sql += f"{col} FLOAT, "
            else:
                sql += f"{col} TEXT, "  # Use TEXT for all other types
        sql = sql.rstrip(", ")  # Remove the trailing comma and space
        sql += ")"
        return sql

    # Generate an INSERT INTO statement based on the DataFrame columns
    def generate_insert_sql(table_name, df):
        columns = ", ".join(df.columns)
        values = ", ".join(["%s"] * len(df.columns))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        return sql
    

    try:
     # Check if the table already exists, drop it if it does
        if check_table_exists(cursor, table_name):
            cursor.execute(f"DROP TABLE {table_name}")
            print(f"Table '{table_name}' dropped successfully.")

        # Create the table
        create_table_sql = generate_create_table_sql(table_name, df)
        cursor.execute(create_table_sql)
        print(f"Table '{table_name}' created successfully.")

        # Insert data into the table
        insert_sql = generate_insert_sql(table_name, df)
        for row in df.itertuples(index=False, name=None):
            cursor.execute(insert_sql, row)
        conn.commit()
        print(f"Data inserted successfully into '{table_name}'.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"MySQL Error: {err.msg}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()