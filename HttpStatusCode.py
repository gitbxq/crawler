# -*- coding:utf-8 -*-
import requests
import sys

def getHttpStatusCode(url):
    userAgent = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"} # 添加一个user-agent,访问反爬虫策略严格的网站很有用
    timeOut = 4 # 请求超时时间设置为4秒
    try:
        request = requests.get(url, headers = userAgent, timeout = timeOut)
        httpStatusCode = request.status_code
        return httpStatusCode
 
    except requests.exceptions.HTTPError as e:
        return e
 
if __name__ == "__main__":
    file = open('linkResult.txt','r')
    for link in file:
        url = link.strip('\n')
        status = getHttpStatusCode(url)
        with open('linkresult.txt','a') as f:
            line = url + '\t//status_code:' + str(status) + '\n'
            f.write(line)