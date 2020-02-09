import configparser
import hashlib

import os
import requests
from lxml import etree

from Entity import Video
from SqlUtils import SqlUtils


class bidong:
    @staticmethod
    def getList(url):
        response = requests.get(url)  # 发get请求
        html = etree.HTML(response.text, etree.HTMLParser())
        href_list = html.xpath('//ul[@id= "chapterList"]//li//a/@href')
        title_list = html.xpath('//ul[@id= "chapterList"]//li//a/text()')
        for index in range(len(href_list)):
            if index < 92:
                continue
            href = 'http://www.bidongmh.com' + href_list[index]
            title = title_list[index]
            if "-" in title:
                title = "".join(title.split())
                title = title[0: title.index("-")]
            response_content_page = requests.get(href)  # 发get请求
            html_content_page = etree.HTML(response_content_page.text, etree.HTMLParser())
            pic_url_list = html_content_page.xpath('//div[@class="comiclist"]//img[@class="comicimg"]/@src')
            for i in range(len(pic_url_list)):
                bidong.download_img_bidong(title, pic_url_list[i], i)
            print(title+ "下载完成")
        print("全部下载完成")
        # title = getArrayFirst(html, '//h3[@class="post-title text"]/a/text()')
        # identifier_web = getArrayFirst(html, '//div[@id="video_id"]//td[@class="text"]/text()')
        # publish_time = getArrayFirst(html, '//div[@id="video_date"]//td[@class="text"]/text()')
        # video_length = getArrayFirst(html, '//div[@id="video_length"]//span[@class="text"]/text()')
        # video_director = getArrayFirst(html,'//span[@class="director"]/a/text()')
        # video_zhizuoshang = getArrayFirst(html,'//span[@class="maker"]/a/text()')
        # video_faxingshang =getArrayFirst(html,'//span[@class="label"]/a/text()')
        # video_score = getArrayFirst(html,'//span[@class="score"]/text()')
        # video_tag = getArrayAll(html,'//span[@class="genre"]/a/text()')
        # actor_name = getArrayAll(html,'//span[@class="cast"]/span/a/text()')
        # img_url = 'http:' + getArrayFirst(html,'//img[@id="video_jacket_img"]/@src')

    @staticmethod
    def download_img_bidong(folder_name, img_url, img_name):
        print(img_url)
        r = requests.get(img_url, stream=True)
        print(r.status_code)  # 返回状态码
        if r.status_code == 200:
            path = 'H:\\bidong\\{}'.format(folder_name)
            file_path = 'H:\\bidong\\{}\\{}.jpg'.format(folder_name, str(img_name))
            if not os.path.exists(path):
                os.makedirs(path)
            open(file_path, 'wb').write(r.content)  # 将内容写入图片
            print("done: "+file_path)
        del r


if __name__ == "__main__":
    url = 'http://www.bidongmh.com/book/9'
    bidong.getList(url)
