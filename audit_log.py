from typing import Optional

from aleph import Aleph
from findings import Finding


class AuditLog:
    def __init__(self, audit_id: int, user_id: int, action: str, timestamp: str, object_type: str, object_id: int,
                 details: str, ip_address: str, device_type: str, browser: str, os: str, city: str, success: bool,
                 error_message: str, request_duration_ms: int, request_size_bytes: int, response_size_bytes: int,
                 response_code: int, referrer: str, user_agent: str, server_ip: str, server_name: str,
                 server_location: str, server_timezone: str, server_version: str, server_status: str,
                 server_logs: str, additional_info: str, aleph: dict, findings: dict) -> None:
        self.audit_id = audit_id
        self.user_id = user_id
        self.action = action
        self.timestamp = timestamp
        self.object_type = object_type
        self.object_id = object_id
        self.details = details
        self.ip_address = ip_address
        self.device_type = device_type
        self.browser = browser
        self.os = os
        self.city = city
        self.success = success
        self.error_message = error_message
        self.request_duration_ms = request_duration_ms
        self.request_size_bytes = request_size_bytes
        self.response_size_bytes = response_size_bytes
        self.response_code = response_code
        self.referrer = referrer
        self.user_agent = user_agent
        self.server_ip = server_ip
        self.server_name = server_name
        self.server_location = server_location
        self.server_timezone = server_timezone
        self.server_version = server_version
        self.server_status = server_status
        self.server_logs = server_logs
        self.additional_info = additional_info
        self.aleph = aleph
        self.findings = findings


def map_to_audit_logs(log: dict, aleph: Aleph, findings: Optional[Finding]) -> AuditLog:
    new_audit_log = AuditLog(
        log.get('AuditID'),
        log.get('User_Id'),
        log.get('Action'),
        log.get('timestamp'),
        log.get('object_type'),
        log.get('object_id'),
        log.get('details'),
        log.get('ipadress'),
        log.get('device_type'),
        log.get('Browser'),
        log.get('os'),
        log.get('City'),
        log.get('succses'),
        log.get('error_message'),
        log.get('request_duration_ms'),
        log.get('request_size_bytes'),
        log.get('response_size_bytes'),
        log.get('response_code'),
        log.get('referrer'),
        log.get('user_agent'),
        log.get('server_ip'),
        log.get('server_name'),
        log.get('server_location'),
        log.get('server_timezone'),
        log.get('server_version'),
        log.get('server_status'),
        log.get('server_logs'),
        log.get('additional_info'),
        aleph.to_dict() if aleph else None,
        findings.to_dict() if findings else None
    )

    return new_audit_log
