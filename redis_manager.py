import json
import logging
import redis
from redis import RedisError
from abc import ABC, abstractmethod


class RedisWriter(ABC):
    @abstractmethod
    def write_to_redis(self, ip_address: str, data: dict) -> None:
        pass


class RedisReader(ABC):
    @abstractmethod
    def get_from_redis(self, key):
        pass


class RedisManager(RedisWriter, RedisReader):
    def __init__(self, redis_host, redis_port, redis_db) -> None:
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
        self.logger = logging.getLogger(__name__)

    def write_to_redis(self, ip_address: str, data: dict) -> None:
        try:
            self.redis_client.set(ip_address, json.dumps(data, ensure_ascii=False))
        except RedisError as e:
            self.logger.error(f"Error setting data in Redis for IP {ip_address}: {e}")

    def get_from_redis(self, key: str) -> bytes:
        return self.redis_client.get(key)
