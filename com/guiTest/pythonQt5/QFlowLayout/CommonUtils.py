import configparser
import hashlib
import sqlite3

import Const


def file_md5(filename):
    hmd5 = hashlib.md5()
    fp = open(filename, 'rb')
    hmd5.update(fp.read())
    return hmd5.hexdigest()


def read_config():
    config = configparser.ConfigParser()
    config.read('setting.ini', encoding='UTF-8')
    return config


def hash_exists(hash_code):
    conn = sqlite3.connect(Const.Gl_db_name)
    cursor = conn.cursor()
    sql_cmd = '''select id from video where hash = '%s' ''' % hash_code
    cursor.execute(sql_cmd)
    res = cursor.fetchall()
    suc = True
    if len(res) > 0:
        print('The hash is exists')
        suc = True
    else:
        print('The hash is NOT exists')
        suc = False
    cursor.close()
    conn.commit()
    conn.close()
    return suc


if __name__ == "__main__":

    print(hash_exists("fffffffffffffffffffff"))
    print(hash_exists("11111111111"))
    print(hash_exists("588ae2a2774ec487a443b1fd9cee6c3c"))
    print(hash_exists("fawfaw33"))
