import redis
from rq import Worker, Connection

listen = ['default']
# url for local redis
redis_url = "redis://localhost:6379"
# url for docker redis
# redis_url = "redis://redis:6379/0"
redis_connection = redis.from_url(redis_url)
with Connection(redis_connection):
    worker = Worker(['default'])
    worker.work()
