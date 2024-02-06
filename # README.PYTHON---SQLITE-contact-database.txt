CHATGPT CONVERSATION 

User
Create a python code that creates a sql database to store contacts 

ChatGPT
Sure, I'll guide you through creating a simple SQL database to store contacts using Python. We'll use SQLite in this example, as it's a lightweight database engine that's included with Python, making it ideal for small projects or for learning purposes.

Here's a step-by-step Python code snippet that creates a SQLite database and a table to store contacts. Each contact will have an ID, name, phone number, and email address.

python
Copy code
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('contacts.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# SQL query to create a table
create_table_query = '''CREATE TABLE IF NOT EXISTS contacts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL);'''

# Execute the SQL query
cursor.execute(create_table_query)

# Commit the changes
conn.commit()

# Function to add a new contact
def add_contact(name, phone, email):
    insert_query = '''INSERT INTO contacts (name, phone, email)
                      VALUES (?, ?, ?);'''
    cursor.execute(insert_query, (name, phone, email))
    conn.commit()

# Example usage
add_contact('John Doe', '123456789', 'john.doe@example.com')

# Close the connection
conn.close()
This code does the following:

Imports the sqlite3 module to work with SQLite database.
Connects to a SQLite database file contacts.db. It creates the file if it doesn't exist.
Creates a cursor object to interact with the database.
Defines a SQL query to create a table named contacts if it doesn't already exist. The table has columns for id (which auto-increments for each new contact), name, phone, and email. The email is set to be unique to avoid duplicate entries.
Executes the query to create the table.
Commits the changes to the database to ensure they are saved.
Defines a function add_contact() to insert a new contact into the database. The function takes name, phone, and email as arguments and uses a parameterized query to insert the data, which helps prevent SQL injection attacks.
Adds an example contact to the database using the add_contact() function.
Closes the database connection.
Remember, you can customize the contacts table structure based on your specific needs, adding or removing columns as necessary. ☺✨






