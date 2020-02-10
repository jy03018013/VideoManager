class Video(object):
    @classmethod
    def test(self):
        return self("1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21")

    def new_video_with_hash(self, hash, ):
        return self("1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21")

    def __init__(self, id, series, identifier, type, video_name_local, actor_name,
                 custom_tag, country, video_path, img_url, img_type,
                 hash, is_download, title, video_director, publish_time,
                 video_length, video_zhizuoshang, video_faxingshang, video_score, video_tag, intro, like_stars,identifier_web,resolution,create_time):
        self.id = id
        self.series = series
        self.identifier = identifier
        self.type = type
        self.video_name_local = video_name_local
        self.actor_name = actor_name
        self.custom_tag = custom_tag
        if custom_tag != None:
            if custom_tag.startswith(","):
                self.custom_tag = custom_tag.replace(",", "", 1)
        self.country = country
        self.video_path = video_path
        self.img_url = img_url
        self.img_type = img_type
        self.hash = hash
        self.is_download = is_download
        self.title = title
        self.video_director = video_director
        self.publish_time = publish_time
        self.video_length = video_length
        self.video_zhizuoshang = video_zhizuoshang
        self.video_faxingshang = video_faxingshang
        self.video_score = video_score
        self.video_tag = video_tag
        self.intro = intro
        self.like_stars = like_stars
        self.identifier_web = identifier_web
        self.resolution = resolution
        self.create_time = create_time
