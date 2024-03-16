import json
from kafka import KafkaConsumer


def consume_from_kafka(kafka_bootstrap_servers, kafka_topic):
    # create KafkaConsumer
    consumer = KafkaConsumer(kafka_topic,
                             bootstrap_servers=kafka_bootstrap_servers,
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=5000,
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    # read messages from kafka
    for message in consumer:
        data = message.value
        print(data)


def main():
    kafka_bootstrap_servers = 'localhost:9092'
    kafka_topic = 'enriched_logs'

    consume_from_kafka(kafka_bootstrap_servers, kafka_topic)


if __name__ == "__main__":
    main()
