import imp
from importlib.resources import contents
import requests
import re
import time

headers = {
    "User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
}

f = open('C:/Users/Administrator/Desktop/Python/doupo.txt','a+')

def get_info(url):
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>',res.content.decode('utf-8'), re.S)
        for content in contents:
            f.write(content +'\n')
    else:
        pass

if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(1,1647)]
    for url in urls:
        get_info(url)
        time.sleep(1)

f.close()