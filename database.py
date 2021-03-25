
import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()