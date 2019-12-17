import sqlite3
from sqlite3 import IntegrityError

import Const
from QFlowLayout import Entity


class SqlUtils:
    @staticmethod
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

    @staticmethod
    def insert_video(sql, parameters):
        try:
            conn = sqlite3.connect(Const.Gl_db_name)
            c = conn.cursor()
            c.execute(sql, parameters)
            conn.commit()
            conn.close()
        except IntegrityError:
            # todo
            print("Hash 重复，不写入")
            pass
        else:
            print("插入成功")

    @staticmethod
    def select_videos(sql):
        video_list = []
        conn = sqlite3.connect(Const.Gl_db_name)
        c = conn.cursor()
        cursor = c.execute(sql)
        for row in cursor:
            video = Entity.Video(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                 row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                                 row[15], row[16], row[17], row[18], row[19], row[20])
            video_list.append(video)
        conn.close()
        return video_list


if __name__ == "__main__":
    video_list = SqlUtils.select_videos("SELECT * from video")
    print()
