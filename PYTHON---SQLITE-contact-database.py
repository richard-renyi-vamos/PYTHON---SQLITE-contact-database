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
