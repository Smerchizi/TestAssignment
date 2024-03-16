import json
from kafka import KafkaProducer


def publish_logs(log_file, kafka_topic, kafka_bootstrap_servers):
    producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    with open(log_file, 'r') as file:
        log_data = json.load(file)

        for log_entry in log_data:
            producer.send(kafka_topic, value=log_entry)
        print("Data sent to Kafka")

    producer.flush()


def main():
    kafka_bootstrap_servers = 'localhost:9092'
    kafka_topic = 'raw_logs'

    log_file_path = '../ha_logs.json'

    publish_logs(log_file_path, kafka_topic, kafka_bootstrap_servers)


if __name__ == "__main__":
    main()
