import json
import sqlite3


conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Execute a SELECT statement to get the data you want to export
cursor.execute('SELECT * FROM kayaks')

# Fetch all rows from the SELECT statement
rows = cursor.fetchall()

# Convert the rows to a list of dictionaries, where each dictionary represents a row
data = [dict(zip([key[0] for key in cursor.description], row)) for row in rows]

# Open a file for writing in binary mode
with open('data.json', 'wb') as f:
  # Use the json.dump function to write the data to the file
  json.dump(data, f)

# Close the file and the database connection
f.close()
conn.close()