# Author: Allen Anker
# Created by Allen Anker on 14/08/2018
import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Allen', 19])
    writer.writerow(['10002', 'Anker', 19])
    writer.writerow(['10003', 'Oliver', 21])
    writer.writerows([['10003', 'Oliver', 21], ['10003', 'Oliver', 21]])

# DictWriter
with open('data.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Allen', 'age': 19})
    writer.writerow({'id': '10002', 'name': 'Allen', 'age': 19})
    writer.writerow({'id': '10003', 'name': 'Allen', 'age': 19})

# reader
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
    print('=' * 50)

import pandas as pd

df = pd.read_csv('data.csv')
print(df)
