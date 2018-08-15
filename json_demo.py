# Author: Allen Anker
# Created by Allen Anker on 14/08/2018
import json

str = '''
[{
    "name": "Allen",
    "gender": "Male",
    "birthday": ""
}, {
    "name": "Anker",
    "gender": "Male",
    "birthday": ""
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
