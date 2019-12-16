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
            id = row[0]
            type = row[1]
            video_name = row[2]
            actor_name = row[3]
            tag = row[4]
            country = row[5]
            company = row[6]
            series = row[7]
            hash = row[8]
            video_path = row[9]
            img_path = row[10]
            img_type = row[11]
            video = Entity.Video(id, type, video_name, actor_name, tag, country, company, series, hash, video_path,
                                 img_path, img_type)
            video_list.append(video)
        conn.close()
        return video_list


if __name__ == "__main__":
    video_list = SqlUtils.select_videos("SELECT * from video")
    print()
