import sqlite3

from QFlowLayout import Entity


class SqlUtils:
    @staticmethod
    def insert_video(sql, parameters):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute(sql, parameters)
        conn.commit()
        conn.close()

    @staticmethod
    def select_videos(sql):
        video_list = []
        conn = sqlite3.connect('test.db')
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
