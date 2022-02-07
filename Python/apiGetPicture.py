from urllib import request
import requests

"""
from urllib.request import urlretrieve
path = 'I:/GitHub/Note/Python/'
url = 'https://alifei04.cfp.cn/creative/vcg/800/version23/VCG41175510742.jpg'

res = requests.get(url)
picturename = url.split('/')[-1]
urlretrieve(url, path+picturename)
"""

headers = {
    "User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
}

path = 'I:/GitHub/Note/Python/'
url = 'https://alifei04.cfp.cn/creative/vcg/800/version23/VCG41175510742.jpg'
picturename = url.split('/')[-1]
data = requests.get(url, headers=headers)
fp = open(path + picturename, 'wb')
fp.write(data.content)
fp.close()
