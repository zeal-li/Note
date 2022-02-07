from email.mime import image
from bs4 import BeautifulSoup
import requests

headers = {
    "User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
}

url_path = 'https://list.jd.com/list.html?cat=670%2C677%2C11303&page=1&s=1&click=0'
wb_data = requests.get(url_path, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
imgs = soup.select('#J_goodsList > ul > li > div > div.p-img > a > img')

list = []
for img in imgs:
    print(img)
    photo = img.get('data-lazy-img')
    list.append(photo)

path = 'I:/GitHub/Note/Python/apiGetPicture2/'
for item in list:
    url = 'http:'+item
    data = requests.get(url, headers=headers)
    picturename = item.split('/')[-1]
    fp = open(path + picturename, 'wb')
    fp.write(data.content)
    fp.close()
