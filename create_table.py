import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE Users (name TEXT, age INTEGER, occupation TEXT,salary REAL,email TEXT,password TEXT)')
print("Created table successfully!")

conn.close()
