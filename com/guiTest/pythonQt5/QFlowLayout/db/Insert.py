import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("INSERT INTO video (type,video_name,actor_name,tag,country,company,series,hash) \
      VALUES (1, '三少爷的剑','李宇春', '武侠', '中国','八一电影','红色系列','gesgwagagwagawg' )");

c.execute("INSERT INTO video (type,video_name,actor_name,tag,country,company,series,hash) \
      VALUES (0, '多情公子无情剑','梁静茹', '剧情', '中国','八一电影','红色系列','rhredhrdhwehw' )");

c.execute("INSERT INTO video (type,video_name,actor_name,tag,country,company,series,hash) \
      VALUES (1, '天下无贼','蔡国庆', '穿越', '法国','八一电影','红色系列','tjherjrdhwetdsgse' )");

c.execute("INSERT INTO video (type,video_name,actor_name,tag,country,company,series,hash) \
      VALUES (0, '罗马假日','刘德华', '现代', '美国','好莱坞','浪漫回忆','segsehsehsesgsegse' )");

conn.commit()
conn.close()
