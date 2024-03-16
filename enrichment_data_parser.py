import json
import logging
from redis_manager import RedisManager


class EnrichmentDataParser:
    def __init__(self, redis_manager: RedisManager) -> None:
        self.redis_manager = redis_manager
        self.logger = logging.getLogger(__name__)

    def parse_enrichment_data(self, file_path: str) -> None:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                enrichment_data = json.load(file)
        except FileNotFoundError as e:
            self.logger.error(f"File not found: {file_path}")
            return
        except json.JSONDecodeError as e:
            self.logger.error(f"Error decoding JSON from file {file_path}: {e}")
            return

        for ip_address, data in enrichment_data.items():
            self.redis_manager.write_to_redis(ip_address, data)

        self.logger.info("Enrichment data written to Redis")
