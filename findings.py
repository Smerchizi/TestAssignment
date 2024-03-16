class Finding:
    def __init__(self, ip_address: str, city: str, country: str, latitude: float, longitude: float, postal_code: str,
                 timezone: str, region_code: str, isp: str,
                 connection_type: str) -> None:
        self.ip_address = ip_address
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.postal_code = postal_code
        self.timezone = timezone
        self.region_code = region_code
        self.isp = isp
        self.connection_type = connection_type

    def to_dict(self) -> dict:
        return vars(self)


def map_to_findings(ip_address: str, json_dict: dict) -> Finding:
    new_findings = Finding(
        ip_address,
        json_dict.get('city'),
        json_dict.get('country'),
        json_dict.get('latitude'),
        json_dict.get('longitude'),
        json_dict.get('postal_code'),
        json_dict.get('timezone'),
        json_dict.get('region_code'),
        json_dict.get('isp'),
        json_dict.get('connection_type')
    )

    return new_findings
