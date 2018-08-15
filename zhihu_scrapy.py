# Author: Allen Anker
# Created by Allen Anker on 14/08/2018
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/53.0.2785.116 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 50 + '\n')
