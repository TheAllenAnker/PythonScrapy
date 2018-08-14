# Author: Allen Anker
# Created by Allen Anker on 13/08/2018
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)