from SqlUtils import SqlUtils

if __name__ == "__main__":
    video_list = SqlUtils._select_("SELECT * from video ")
    print()