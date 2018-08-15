# Author: Allen Anker
# Created by Allen Anker on 15/08/2018
import requests

'''
url = 'http://localhost:8050/render.html?url=https://www.baidu.com&wait=5'
response = requests.get(url)
print(response.text)
'''

url = 'http://localhost:8050/render.png?url=https://www.baidu.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('baidu.png', 'wb') as f:
    f.write(response.content)
