from enum import Enum


class InfrastructureException(Exception):

    class ErrorType(Enum):
        UNKNOWN = 0
        REQUEST_ERROR = 1
        FAILED = 2

    def __init__(self, error_type: ErrorType = ErrorType.REQUEST_ERROR, message: str = ''):
        self.error_type = error_type
        self.message = message
