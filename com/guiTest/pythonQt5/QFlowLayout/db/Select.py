import sqlite3

conn = sqlite3.connect(Const.Gl_db_name)
c = conn.cursor()

cursor = c.execute("SELECT id,type,video_name,actor_name,tag,country,company,series,hash  from video")
for row in cursor:
    print("id = ", row[0])

    print("type = ", row[1])

    print("video_name = ", row[2])

    print("actor_name = ", row[3])

    print("tag = ", row[4])

    print("country = ", row[5])

    print("company = ", row[6])

    print("series = ", row[7])

    print("hash = ", row[8], "\n")


print
"Operation done successfully";
conn.close()
