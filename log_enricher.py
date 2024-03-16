import logging
import json
from utils import find_ip_address
from typing import Optional
from redis_manager import RedisManager
from audit_log import map_to_audit_logs
from aleph import map_to_aleph
from findings import map_to_findings

class LogEnricher:
    def __init__(self, redis_manager: RedisManager) -> None:
        self.redis_manager = redis_manager
        self.logger = logging.getLogger(__name__)

    def enrich_log(self, logs: list) -> list:
        enriched_logs = []
        for log_entry in logs:
            ip_address = find_ip_address(log_entry)
            aleph = map_to_aleph(log_entry)
            findings_data = self.get_enrichment_data(ip_address)
            findings = map_to_findings(ip_address, findings_data) if findings_data else {}
            audit_log = map_to_audit_logs(log_entry, aleph, findings)

            enriched_log_entry = {
                'audit_log': audit_log.__dict__
            }

            enriched_logs.append(enriched_log_entry)
        self.logger.info("Logs enriched")
        return enriched_logs

    def get_enrichment_data(self, ip_address: str) -> Optional[dict]:
        enrichment_data_json = self.redis_manager.get_from_redis(ip_address)

        if enrichment_data_json:
            self.logger.info("Enrichment data retrieved from Redis")
            return json.loads(enrichment_data_json)
        else:
            self.logger.warning(f"No enrichment data found for IP address: {ip_address}")
            return None

