import logging
import os
from redis_manager import RedisManager
from enrichment_data_parser import EnrichmentDataParser
from kafka_log_consumer import LogRetriever
from log_enricher import LogEnricher
from json_writer import JsonWriter
from kafka_producer_enriched_logs import KafkaProducerEnrichedLogs


# 234.234.50.133

def main():
    logging.basicConfig(filename='app_logs.log', level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    redis_host = os.getenv('REDIS_HOST', 'localhost')
    redis_port = os.getenv('REDIS_PORT', 6379)
    redis_db = os.getenv('REDIS_DB', 0)
    enrichment_file_path = os.getenv('ENRICHMENT_FILE_PATH', 'enrichment.json')
    kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    kafka_topic_producer = os.getenv('KAFKA_TOPIC_PRODUCER', 'enriched_logs')

    redis_manager = RedisManager(redis_host, redis_port, redis_db)
    enrichment_data_parser = EnrichmentDataParser(redis_manager)
    log_retriever = LogRetriever(redis_manager, kafka_bootstrap_servers, 'raw_logs')
    log_enricher = LogEnricher(redis_manager)
    json_writer = JsonWriter()
    kafka_producer = KafkaProducerEnrichedLogs(kafka_bootstrap_servers)

    enrichment_data_parser.parse_enrichment_data(enrichment_file_path)
    while True:
        logs = log_retriever.retrieve_logs()
        if logs:
            enriched_logs = log_enricher.enrich_log(logs)
            file = json_writer.write_to_json(enriched_logs)
            kafka_producer.send_json_file_to_kafka(file, kafka_topic_producer)

        print("iteration complete")

if __name__ == "__main__":
    main()
