from kafka import KafkaProducer
import json
import logging


class KafkaProducerEnrichedLogs:
    def __init__(self, bootstrap_servers: str) -> None:
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        self.logger = logging.getLogger(__name__)

    def send_json_file_to_kafka(self, json_file_path: str, kafka_topic: str) -> None:
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError as e:
            self.logger.error(f"File not found: {json_file_path}")
            return
        except json.JSONDecodeError as e:
            self.logger.error(f"Error decoding JSON file {json_file_path}: {e}")
            return

        for log_entry in data:
            self.producer.send(kafka_topic, value=json.dumps(log_entry).encode('utf-8'))

        self.producer.flush()
        # self.producer.close()

        self.logger.info("Message sent to Kafka")
