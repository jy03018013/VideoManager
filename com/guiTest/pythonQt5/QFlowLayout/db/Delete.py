import sqlite3

import Const

conn = sqlite3.connect(Const.Gl_db_name)
c = conn.cursor()
print
"Opened database successfully";

c.execute("DELETE FROM COMPANY WHERE ID=2;")
conn.commit()
print
"Total number of rows deleted :", conn.total_changes

cursor = conn.execute("SELECT id, name, address, salary  FROM COMPANY")
for row in cursor:
    print
    "ID = ", row[0]
    print
    "NAME = ", row[1]
    print
    "ADDRESS = ", row[2]
    print
    "SALARY = ", row[3], "\n"

print
"Operation done successfully";
conn.close()
