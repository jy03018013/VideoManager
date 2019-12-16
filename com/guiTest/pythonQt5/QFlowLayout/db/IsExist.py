import sqlite3

conn = sqlite3.connect('/tmp/urls.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS  urls (id integer primary key autoincrement, link text)')

def url_exists(url):
    sql_cmd = '''select * from urls where link = '%s' ''' % url
    cursor.execute(sql_cmd)
    res = cursor.fetchall()
    suc = True
    if len(res) > 0 :
        print ('%s exists' % url)
        suc = True
    else:
        sql_cmd_2 = '''insert into urls(link) values('%s') ''' % url
        cursor.execute(sql_cmd_2)
        print ('%s added' % url)
        suc = False
    cursor.close()
    conn.commit()
    conn.close()
    return suc


url_status = url_exists('example.com')
print (url_status)