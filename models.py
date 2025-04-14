
from datetime import datetime

class Goal:
    required_fields = ['title', 'type', 'description']
    types = ['daily', 'weekly', 'monthly']

    @staticmethod
    def validate(data):
        if not all(field in data for field in Goal.required_fields):
            return False
        if data['type'] not in Goal.types:
            return False
        return True

class Reflection:
    required_fields = ['rating', 'notes']

    @staticmethod
    def validate(data):
        if not all(field in data for field in Reflection.required_fields):
            return False
        if not isinstance(data['rating'], int) or not (1 <= data['rating'] <= 5):
            return False
        return True
