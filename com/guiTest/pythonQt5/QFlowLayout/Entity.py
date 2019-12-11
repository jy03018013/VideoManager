class Video(object):
    def __init__(self, id, type, video_name, actor_name, tag, country, company, series, hash, video_path, img_path,
                 img_type):
        self.id = id
        self.type = type
        self.video_name = video_name
        self.actor_name = actor_name
        self.tag = tag
        self.country = country
        self.company = company
        self.series = series
        self.hash = hash
        self.video_path = video_path
        self.img_path = img_path
        self.img_type = img_type
