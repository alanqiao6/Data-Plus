import mysql.connector

# Create Database (only run once)
"""
mydb = mysql.connector.connect(
    host="localhost",
    user="ignite",
    password='ignite'
)

mycursor.execute("CREATE DATABASE mydatabase")
"""


# Connect to Database
mydb = mysql.connector.connect(
    host="localhost",
    user="ignite",
    password='ignite',
    database="mydatabase"
)


mycursor = mydb.cursor()


# Print Databases
"""
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
"""

"""
# Create Table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Check if Table Exists
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
"""

"""
# Create NEW table with Primary Key (ID numbers, this gives autofill)
mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255)")

# Add Primary Key to Existing Table
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
"""

"""
# Insert Into Table (1 record)
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted")

# Insert Multiple Rows
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)
val = [
('Peter', 'Lowstreet 4'),
('Amy', 'Apple st 652'),
('Hannah', 'Mountain 21'),
('Michael', 'Valley 345'),
('Sandy', 'Ocean blvd 2'),
('Betty', 'Green Grass 1'),
('Richard', 'Sky st 331'),
('Susan', 'One way 98'),
('Vicky', 'Yellow Garden 2'),
('Ben', 'Park Lane 38'),
('William', 'Central st 954'),
('Chuck', 'Main Road 989'),
('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
]"""

"""
# Get Inserted ID

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
"""

"""
# Select From Table
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Select Columns
mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Select One Row
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)

# Select with a Filter
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Wildcard uses %- start, include, or end in phrase
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

"""

"""
# Delete Record- MUST HAVE WHERE OR ELSE ALL DELETE!
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
"""

"""
# Update Record
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
"""