import sqlite3
from sqlite3 import IntegrityError

import Const
from QFlowLayout import Entity


class SqlUtils:
    @staticmethod
    def hash_exists(hash_code):
        conn = sqlite3.connect(Const.Gl_db_name)
        cursor = conn.cursor()
        sql_cmd = '''select video_path from video where hash = '%s' ''' % hash_code
        cursor.execute(sql_cmd)
        res = cursor.fetchall()
        suc = True
        path = ''
        if len(res) > 0:
            print('The hash is exists')
            path = res[0][0]
            suc = True
        else:
            print('The hash is NOT exists')
            suc = False
        cursor.close()
        conn.commit()
        conn.close()
        return suc, path

    @staticmethod
    def delete_video(hash):
        conn = sqlite3.connect(Const.Gl_db_name)
        sql = '''DELETE FROM video WHERE hash = '%s' ''' % hash
        conn.cursor().execute(sql)
        conn.commit()
        conn.close()

    @staticmethod
    def update_video(sql, parameters):
        try:
            conn = sqlite3.connect(Const.Gl_db_name)
            cursor = conn.cursor()
            cursor.execute(sql, parameters)
            conn.commit()
            conn.close()
        except IntegrityError:
            # todo
            print("Hash 重复，不写入")
            pass
        else:
            print("更新成功")

    @staticmethod
    def select_videos(sql):
        video_list = []
        conn = sqlite3.connect(Const.Gl_db_name)
        c = conn.cursor()
        cursor = c.execute(sql)
        for row in cursor:
            video = Entity.Video(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                 row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                                 row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23],
                                 row[24], row[25])
            video_list.append(video)
        conn.close()
        return video_list

    @staticmethod
    def _select_(sql):
        entity_list = []
        conn = sqlite3.connect(Const.Gl_db_name)
        c = conn.cursor()
        cursor = c.execute(sql)
        for row in cursor:
            entity = []
            for danyuan in row:
                entity.append(danyuan)
            entity_list.append(entity)
        conn.close()
        return entity_list


if __name__ == "__main__":
    video_list = SqlUtils._select_("SELECT * from video ")
    print()
