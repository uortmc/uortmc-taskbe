from .base import TaskbeException


class TokenValidationViolation(TaskbeException):
    def __init__(self):
        super(TokenValidationViolation, self).__init__("Given token already exists or invalid")

class ImageBase64DecodeException(TaskbeException):
    def __init__(self):
        super(ImageBase64DecodeException,self).__init__("Given image base64 string wasn't decoded successfully, "
                                                        "possibly corrupt data?")

class ScanNotFound(TaskbeException):
    def __init__(self):
        super(ScanNotFound, self).__init__("Given scan token not found")

