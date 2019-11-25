import requests
keyword = "Python"
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params=kv) 
    print(r.request.url)  # http://www.baidu.com/s?wd=Python
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
