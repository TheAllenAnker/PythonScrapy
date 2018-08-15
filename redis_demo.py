# Author: Allen Anker
# Created by Allen Anker on 14/08/2018
from redis import StrictRedis, ConnectionPool

'''
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', 'Allen')
print(redis.get('name'))
'''

# using connection pool
'''
pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)
'''

url = 'redis://:@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
redis.set('name', 'Allen')
print(redis.get('name'))