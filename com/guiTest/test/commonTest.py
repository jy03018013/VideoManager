import requests

url='http://www.h28o.com/cn/vl_searchbyid.php?keyword=IPX-316'
r = requests.get(url) #发get请求
print(r)#返回<Response [200]>
# print(r.json())#将返回的json串转为字典
print(r.text)#返回get到的页面的返回数据