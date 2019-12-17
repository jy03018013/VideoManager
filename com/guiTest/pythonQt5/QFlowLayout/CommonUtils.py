import configparser
import hashlib
import requests
from lxml import etree

from Entity import Video


def file_md5(filename):
    hmd5 = hashlib.md5()
    fp = open(filename, 'rb')
    hmd5.update(fp.read())
    return hmd5.hexdigest()


def read_config():
    config = configparser.ConfigParser()
    config.read('setting.ini', encoding='UTF-8')
    return config


def get_video_info(identifier: str, video: Video):
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
    video.title = html.xpath('//h3[@class="post-title text"]/a/text()')
    identifier_web = html.xpath('//div[@id="video_id"]//td[@class="text"]/text()')
    video.publish_time = html.xpath('//div[@id="video_date"]//td[@class="text"]/text()')
    video.video_length = html.xpath('//div[@id="video_length"]//span[@class="text"]/text()')
    video.video_director = html.xpath('//span[@class="director"]/a/text()')
    video.video_zhizuoshang = html.xpath('//span[@class="maker"]/a/text()')
    video.video_faxingshang = html.xpath('//span[@class="label"]/a/text()')
    video.video_score = html.xpath('//span[@class="score"]/text()')
    video.video_tag = html.xpath('//span[@class="genre"]/a/text()')
    video.actor_name = html.xpath('//span[@class="cast"]/span/a/text()')
    # print(response)  # 返回<Response [200]>
    # print(response.text)  # 返回get到的页面的返回数据


def download_img(img_url):
    print(img_url)
    r = requests.get(img_url, stream=True)
    print(r.status_code)  # 返回状态码
    if r.status_code == 200:
        open('cache/coverimg/img.jpg', 'wb').write(r.content)  # 将内容写入图片
        print("done")
    del r


if __name__ == '__main__':
    # 下载要的图片
    img_url = "http://img12.3lian.com/gaoqing02/02/93/37.jpg"
    download_img(img_url)

if __name__ == "__main__":
    video = Video.test()
    get_video_info("dpmi-001", video)
