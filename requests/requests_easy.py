import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        # https://2.python-requests.org/en/master/user/quickstart/#response-status-codes
        r.raise_for_status()
        print(r.apparent_encoding)
        print(r.encoding)
        print(r.headers)
        # https://2.python-requests.org/en/master/api/#requests.Response.apparent_encoding
        r.encoding = r.apparent_encoding
        # https://2.python-requests.org/en/master/api/#requests.Response.text
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
