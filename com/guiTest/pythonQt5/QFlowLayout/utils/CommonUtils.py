import configparser
import hashlib
import requests
from bs4 import BeautifulSoup
from lxml import etree
from requests.adapters import HTTPAdapter

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
    config.read('setting.ini', encoding='UTF-8-sig')
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

# javbus网站采集
def get_video_info(identifier: str, hash, downlowd_type: int):
    config = read_config()
    url = config.get('DEFAULT', 'web_site') + "/" + identifier
    session = requests.Session()
    session.mount('http://', HTTPAdapter(max_retries=3))
    session.mount('https://', HTTPAdapter(max_retries=3))
    # response = requests.get(url)  # 发get请求
    response = None
    try:
        response = session.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(e)
    if "404 Page Not Found!" in response.text:
        print(identifier+"：该影片网站未收录或者识别码错误")
        return
    if "识别码搜寻结果" in response.text:
        html = etree.HTML(response.text, etree.HTMLParser())
        url = config.get('DEFAULT', 'web_site') + html.xpath('//div[@class="video"]//a/@href')[0][1:]
        response = requests.get(url)
    html = etree.HTML(response.text, etree.HTMLParser())
    title =getArrayFirst(html,'//div[@class="container"]/h3/text()')
    # span_list = html.xpath('//div[@class="col-md-3 info"]/p/span')
    # a_list = html.xpath('//div[@class="col-md-3 info"]/p/a')
    identifier_web = ''
    publish_time = ''
    video_length = ''
    video_director = ''
    video_zhizuoshang =''
    video_faxingshang =''
    video_score = 0
    soup = BeautifulSoup(response.text, 'lxml')
    for item in soup.select('.col-md-3 p'):
        if '識別碼: ' in item.text:
            identifier_web = item.text.replace('識別碼: ','').replace('\n','')
        if '發行日期: ' in item.text:
            publish_time = item.text.replace('發行日期: ','').replace('\n','')
        if '長度: ' in item.text:
            video_length = item.text.replace('長度: ','').replace('分鐘','')
        if '導演: ' in item.text:
            video_director = item.text.replace('導演: ','').replace('\n','')
        if '製作商: ' in item.text:
            video_zhizuoshang = item.text.replace('製作商: ','').replace('\n','')
        if '發行商: ' in item.text:
            video_faxingshang = item.text.replace('發行商: ','').replace('\n','')
    tag_num = 0
    for item in soup.select('.col-md-3 p'):
        tag_num = tag_num + 1
        if item.text == '類別:':
            break
    video_tag = ''
    try:
        video_tag = soup.select('.col-md-3 p')[tag_num].text.replace('\n',',')
    except:
        pass
    actor_num = 0
    for item in soup.select('.col-md-3 p'):
        actor_num = actor_num + 1
        if item.text == '演員:':
            break
    actor_name = ''
    try:
        actor_name = soup.select('.col-md-3 p')[actor_num].text.replace('\n\n','').replace('\n',',')
    except:
        pass
    actor_name = actor_name + ','
    img_url = soup.select(".bigImage img")[0].attrs.get('src')
    response.close()
    sql = "UPDATE video SET is_download = ?,title = ?,video_director=?,publish_time=?," \
          "video_length=?,video_zhizuoshang=?,video_faxingshang=?,video_score=?," \
          "video_tag=?,actor_name=? ,img_url = ? ,identifier_web=? WHERE hash = ?"
    SqlUtils.update_video(sql, (1, title, video_director, publish_time, video_length,
                                video_zhizuoshang, video_faxingshang, video_score,
                                video_tag, actor_name, img_url,identifier_web, hash))

# javlibrary网站采集
# def get_video_info(identifier: str, hash, downlowd_type: int):
#     config = read_config()
#     url = config.get('DEFAULT', 'web_site') + "/vl_searchbyid.php?keyword=" + identifier
#     response = requests.get(url)  # 发get请求
#     if "搜寻没有结果" in response.text:
#         print("该影片网站未收录")
#         return
#     if "识别码搜寻结果" in response.text:
#         html = etree.HTML(response.text, etree.HTMLParser())
#         url = config.get('DEFAULT', 'web_site') + html.xpath('//div[@class="video"]//a/@href')[0][1:]
#         response = requests.get(url)
#     html = etree.HTML(response.text, etree.HTMLParser())
#     title = getArrayFirst(html, '//h3[@class="post-title text"]/a/text()')
#     identifier_web = getArrayFirst(html, '//div[@id="video_id"]//td[@class="text"]/text()')
#     publish_time = getArrayFirst(html, '//div[@id="video_date"]//td[@class="text"]/text()')
#     video_length = getArrayFirst(html, '//div[@id="video_length"]//span[@class="text"]/text()')
#     video_director = getArrayFirst(html,'//span[@class="director"]/a/text()')
#     video_zhizuoshang = getArrayFirst(html,'//span[@class="maker"]/a/text()')
#     video_faxingshang =getArrayFirst(html,'//span[@class="label"]/a/text()')
#     video_score = getArrayFirst(html,'//span[@class="score"]/text()')
#     video_tag = getArrayAll(html,'//span[@class="genre"]/a/text()')
#     actor_name = getArrayAll(html,'//span[@class="cast"]/span/a/text()')
#     img_url = 'http:' + getArrayFirst(html,'//img[@id="video_jacket_img"]/@src')
#     response.close()
#     sql = "UPDATE video SET is_download = ?,title = ?,video_director=?,publish_time=?," \
#           "video_length=?,video_zhizuoshang=?,video_faxingshang=?,video_score=?," \
#           "video_tag=?,actor_name=? ,img_url = ? ,identifier_web=? WHERE hash = ?"
#     SqlUtils.update_video(sql, (1, title, video_director, publish_time, video_length,
#                                 video_zhizuoshang, video_faxingshang, video_score,
#                                 video_tag, actor_name, img_url,identifier_web, hash))
def getArrayAll(html, path):
    name = ''
    if (len(html.xpath(path)) > 0):
        for tag in html.xpath(path):
            name = name + tag + ","
    return name

def getArrayFirst(html, path):
    name = ''
    if (len(html.xpath(path)) > 0):
        name = html.xpath(path)[0]
    return name


def download_img(video_identifier, img_url):
    try:
        print(img_url)
        response = requests.get(img_url,timeout=10)
        print(response.status_code)  # 返回状态码
        if response.status_code == 200:
            fp = open('cache/coverimg/' + video_identifier + '.jpg', 'wb')# 将内容写入图片
            fp.write(response.content)
            fp.close()
            response.close()
            print("done")
            return True
    except Exception as e:
        print("请求一次"+str(e))
        download_img(video_identifier, img_url)
        pass


# if __name__ == '__main__':
#     # 下载要的图片
#     img_url = "http://img12.3lian.com/gaoqing02/02/93/37.jpg"
#     download_img(img_url)
#
if __name__ == "__main__":
    # video = Video.test()
    get_video_info("IDBD-799", "IDBD-799",1)
