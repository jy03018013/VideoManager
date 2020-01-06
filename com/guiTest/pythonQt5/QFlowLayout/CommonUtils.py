import configparser
import hashlib
import requests
from lxml import etree

from Entity import Video
from SqlUtils import SqlUtils


def file_md5(filename):
    try:
        hmd5 = hashlib.md5()
        fp = open(filename, 'rb')
        hmd5.update(fp.read())
        return hmd5.hexdigest()
    except Exception as e:
        print(e)
        return None


def read_config():
    config = configparser.ConfigParser()
    config.read('setting.ini', encoding='UTF-8')
    return config


def get_setting_ini_(tab, key, default_value):
    try:
        config = read_config()
        return config[tab][key]
    except Exception as e:
        print(e)
        return default_value


def update_setting_ini_(tab, key, value):
    try:
        config = read_config()
        config.set(tab, key, value)
        config.write(open('setting.ini', 'w', encoding='UTF-8'))
    except Exception as e:
        print(e)
        pass


def get_video_info(identifier: str, hash, downlowd_type: int):
    config = read_config()
    url = config.get('DEFAULT', 'web_site') + "/vl_searchbyid.php?keyword=" + identifier
    response = requests.get(url)  # 发get请求
    if "搜寻没有结果" in response.text:
        print("该影片网站未收录")
        return
    if "识别码搜寻结果" in response.text:
        html = etree.HTML(response.text, etree.HTMLParser())
        url = html.xpath('//div[@class="video"]//a/@href')[0]
    html = etree.HTML(response.text, etree.HTMLParser())
    title = html.xpath('//h3[@class="post-title text"]/a/text()')
    identifier_web = html.xpath('//div[@id="video_id"]//td[@class="text"]/text()')
    publish_time = html.xpath('//div[@id="video_date"]//td[@class="text"]/text()')
    video_length = html.xpath('//div[@id="video_length"]//span[@class="text"]/text()')
    video_director = html.xpath('//span[@class="director"]/a/text()')
    video_zhizuoshang = html.xpath('//span[@class="maker"]/a/text()')
    video_faxingshang = html.xpath('//span[@class="label"]/a/text()')
    video_score = html.xpath('//span[@class="score"]/text()')
    video_tag = html.xpath('//span[@class="genre"]/a/text()')
    actor_name = html.xpath('//span[@class="cast"]/span/a/text()')
    img_url = "";

    sql = "UPDATE video SET is_download = ?,title = ?,video_director=?,publish_time=?," \
          "video_length=?,video_zhizuoshang=?,video_faxingshang=?,video_score=?," \
          "video_tag=?,actor_name=? ,img_url = ? WHERE hash = ?"
    SqlUtils.update_video(sql, (1, title, video_director, publish_time, video_length,
                                video_zhizuoshang, video_faxingshang, video_score,
                                video_tag, actor_name, img_url, hash))


def download_img(video_name_local, img_url):
    print(img_url)
    r = requests.get(img_url, stream=True)
    print(r.status_code)  # 返回状态码
    if r.status_code == 200:
        open('cache/coverimg/' + video_name_local + '.jpg', 'wb').write(r.content)  # 将内容写入图片
        print("done")
    del r

# if __name__ == '__main__':
#     # 下载要的图片
#     img_url = "http://img12.3lian.com/gaoqing02/02/93/37.jpg"
#     download_img(img_url)
#
# if __name__ == "__main__":
#     # video = Video.test()
#     get_video_info("dpmi-001", 1)
