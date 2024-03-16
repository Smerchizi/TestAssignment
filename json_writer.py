import json
import logging
from datetime import datetime


class JsonWriter:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def write_to_json(self, data: list) -> str:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output_file = f'enriched_logs_{timestamp}.json'

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except FileNotFoundError as e:
            self.logger.error(f"Error: File not found: {output_file}")
        except IOError as e:
            self.logger.error(f"Error writing file {output_file}: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error occurred: {e}")
        self.logger.info(f"Data written to {output_file}")
        return output_file
