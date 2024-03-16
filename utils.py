from typing import Optional
import re



def find_ip_address(log_entry: dict) -> Optional[str]:
    ip_regex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    for key, value in log_entry.items():
        if isinstance(value, str):
            match = re.search(ip_regex, value)
            if match:
                return match.group(0)

    return None