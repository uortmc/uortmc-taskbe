from .base import TaskbeException


class TokenValidationViolation(TaskbeException):
    def __init__(self):
        super(TokenValidationViolation, self).__init__("Given token already exists or invalid")

class ScanNotFound(TaskbeException):
    def __init__(self):
        super(ScanNotFound, self).__init__("Given scan token not found")