import sqlite3

# Create a database connection
conn = sqlite3.connect('order.db')

# Create a cursor
cursor = conn.cursor()

# Create a Table

#cursor.execute("""CREATE TABLE orders (
# #   name text,
    #category text,
    #quantity int
#)""")



# Commit our command
conn.commit()

# Close our connection
conn.close()
