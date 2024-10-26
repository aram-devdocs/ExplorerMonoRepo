import json


class JSON:
    @staticmethod
    def stringify(obj):
        try:
            return json.dumps(obj)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Object could not be serialized to JSON: {e}")

    @staticmethod
    def parse(json_string):
        try:
            return json.loads(json_string)
        except (TypeError, ValueError) as e:
            raise ValueError(f"String could not be parsed as JSON: {e}")

    @staticmethod
    def stringify_DTO(dto):
        return JSON.stringify(dto.__dict__)
