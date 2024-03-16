

class Aleph:
    def __init__(self, timestamp: str, action: str, object_type: str, success: bool,
                 error_message: str, response_code: int) -> None:
        self.timestamp = timestamp
        self.action = action
        self.object_type = object_type
        self.success = success
        self.error_message = error_message
        self.response_code = response_code

    def to_dict(self) -> dict:
        return vars(self)


def map_to_aleph(log: dict) -> Aleph:
    new_aleph = Aleph(
        log.get('timestamp'),
        log.get('Action'),
        log.get('object_type'),
        log.get('succses'),
        log.get('error_message'),
        log.get('response_code')
    )
    return new_aleph

