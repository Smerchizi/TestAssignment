from kafka import KafkaConsumer
import json
import logging
from redis_manager import RedisManager


class LogRetriever:
    def __init__(self, redis_manager: RedisManager, kafka_bootstrap_servers: str, kafka_topic: str) -> None:
        self.redis_manager = redis_manager
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        self.kafka_topic = kafka_topic
        self.logger = logging.getLogger(__name__)
        self.consumer = KafkaConsumer(self.kafka_topic,
                                     bootstrap_servers=self.kafka_bootstrap_servers,
                                     consumer_timeout_ms=5000)


    def retrieve_logs(self) -> list:

        logs = []

        for message in self.consumer:
            log_entry = json.loads(message.value)
            logs.append(log_entry)

        if logs:
            self.logger.info("Logs retrieved from Kafka")
        else:
            self.logger.warning("No logs retrieved from Kafka")
        return logs
