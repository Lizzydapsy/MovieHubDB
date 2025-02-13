import redis
from config import REDIS_CONFIG

redis_client = redis.StrictRedis(host=REDIS_CONFIG['host'], port=REDIS_CONFIG['port'], decode_responses=True)
