import imp
from pydoc import html
import requests
from lxml import etree
import pymongo
from multiprocessing import Pool

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
jianshu_shouye = mydb['jianshu_shouye']

headers = {
    "User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
}


def get_jianshu_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        try:
            author = info.xpath('div/div/a[1]/text()')
            title = info.xpath('div/a/text()')
            content = info.xpath('div/p/text()')
            data = {
                'author': author,
                'title': title,
                'content': content,
            }
            jianshu_shouye.insert_one(data)
        except IndexError:
            pass


if __name__ == '__main__':
    urls = ['http://www.jianshu.com/c/bDHhpK?order_by=commented_at&page={}'.format(
        str(i)) for i in range(1, 100)]
    pool = Pool(processes=4)
    pool.map(get_jianshu_info, urls)
