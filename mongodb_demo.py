# Author: Allen Anker
# Created by Allen Anker on 14/08/2018
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
# or
client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client.test
collection = db.students
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student1 = {
    'id': '20170102',
    'name': 'Allen',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170103',
    'name': 'Anker',
    'age': 20,
    'gender': 'male'
}
result = collection.insert_one(student)
print(result)
result = collection.insert_many([student1, student2])
print(result)

# update data
condition = {'name': 'Jordan'}
student = collection.find_one(condition)
student['age'] = 18
result = collection.update_one(condition, {'$set': student})
print(result)
