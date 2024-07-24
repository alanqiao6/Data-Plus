import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import numpy as np
import re

# Configuration
database_name = "ignite_data"
config = { 
    'user': "root",
    'password': 'yourPasswordHere', 
    'host': 'localhost',
    'raise_on_warnings': True
}

# Connect to MySQL server (without specifying database)
try:
    conn = mysql.connector.connect(user=config['user'], password=config['password'], host=config['host'], raise_on_warnings=config['raise_on_warnings'])
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

table_names = ['ignite']
csv_file_paths = ["50_score_datasets/final_gui_dataset.csv"]

def check_database_exists(cursor, database_name):
    cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
    result = cursor.fetchone()
    return result is not None

if not check_database_exists(cursor, database_name):
    cursor.execute(f"CREATE DATABASE {database_name}")
    print(f"Database '{database_name}' created successfully.")
else:
    print(f"Database '{database_name}' already exists.")

for i in range(len(table_names)):
    table_name = table_names[i]
    csv_file_path = csv_file_paths[i]

    def check_table_exists(cursor, table_name):
        cursor.execute("SHOW TABLES LIKE %s", (table_name,))
        result = cursor.fetchone()
        return result is not None

    conn.close()
    config['database'] = database_name
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
    except mysql.connector.Error as err:
        print(f"Error reconnecting to database: {err}")
        continue

    try:
        df = pd.read_csv(csv_file_path)
        print(f"Loaded CSV file for table '{table_name}' successfully.")
    except Exception as e:
        print(f"Error loading CSV file for table '{table_name}': {e}")
        continue

    # Drop unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.loc[:, ~df.columns.str.contains('^col_1')]

    def clean_column_name(name, existing_names):
        name = re.sub(r'[^0-9a-zA-Z_]', '', name)
        if re.match(r'^\d', name):  # If the name starts with a digit, prefix it
            name = 'col_' + name
        name = name[:60]
        new_name = name
        count = 1
        while new_name in existing_names:
            new_name = f"{name}_{count}"
            if len(new_name) > 64:
                new_name = new_name[:64 - len(str(count)) - 1] + f"_{count}"
            count += 1
        existing_names.add(new_name)
        return new_name

    existing_names = set()
    df.columns = [clean_column_name(col, existing_names) for col in df.columns]

    # Replace NaN values with None
    df = df.where(pd.notnull(df), None)
    df = df.replace({np.nan: None})

    # Ensure there are no 'nan' strings
    df = df.replace(r'^\s*nan\s*$', None, regex=True)
    df = df.replace(r'^\s*$', 'None', regex=True)

    def generate_create_table_sql(table_name, df):
        sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` ("
        for col in df.columns:
            if pd.api.types.is_integer_dtype(df[col]):
                sql += f"`{col}` INT, "
            elif pd.api.types.is_float_dtype(df[col]):
                sql += f"`{col}` FLOAT, "
            else:
                sql += f"`{col}` TEXT, "
        sql = sql.rstrip(", ")
        sql += ")"
        return sql

    def generate_insert_sql(table_name, df):
        columns = ", ".join([f"`{col}`" for col in df.columns])
        values = ", ".join(["%s"] * len(df.columns))
        sql = f"INSERT INTO `{table_name}` ({columns}) VALUES ({values})"
        return sql

    try:
        if check_table_exists(cursor, table_name):
            cursor.execute(f"DROP TABLE `{table_name}`")
            print(f"Table '{table_name}' dropped successfully.")

        create_table_sql = generate_create_table_sql(table_name, df)
        cursor.execute(create_table_sql)
        print(f"Table '{table_name}' created successfully.")

        insert_sql = generate_insert_sql(table_name, df)
        for row in df.itertuples(index=False, name=None):
            # Convert row values to None where they are NaN or NaT
            row = tuple(None if pd.isna(x) else x for x in row)
            cursor.execute(insert_sql, row)
        conn.commit()
        print(f"Data inserted successfully into '{table_name}'.")

    except mysql.connector.Error as err:
        print(f"MySQL Error for table '{table_name}': {err}")
    except Exception as ex:
        print(f"An error occurred with table '{table_name}': {ex}")

    finally:
        cursor.close()
        conn.close()