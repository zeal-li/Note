import imp
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
headers = {
    "User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
}
res = requests.get('https://list.jd.com/list.html?cat=670,677,11303', headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
#print(soup.prettify())
#print(soup.find('div'))
prices = soup.select('#J_goodsList > ul > li > div > div.p-price > strong > i')
for price in prices:
    print(price.get_text())