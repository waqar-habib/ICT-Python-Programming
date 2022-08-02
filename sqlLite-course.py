import sqlite3

#connects or creates a db
conn = sqlite3.connect('customer.db')

#create a cursor (c)
c = conn.cursor()

# create a table
# DATATYPES = null, real (10.5), integers (10), text (string), blob(images etc..)

# c.execute("""CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text    
# )""")

# insert first entry
# c.execute("INSERT INTO customers (first_name, last_name, email) VALUES ('Waqar', 'Habib', 'waqar@codemy.com')""")

#insert many entries
# many_customers = [
#     ('mahad','abdullah','a.b@t.com'),
#     ('aliya','meher','w.h@t.com'),
#     ('meri','cordaro','m.k@t.com'),
#     ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

# update records
# c.execute("""UPDATE customers SET first_name = 'Waqar' WHERE rowid = 3
       
#           """)


# delete records
# c.execute("""DELETE FROM customers WHERE rowid = 4
        
#           """)

#save to DB
conn.commit()

# # query db
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)



#close connection
conn.close()
