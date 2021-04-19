from .base import TaskbeException
from ..models import Scan


class TokenValidationViolation(TaskbeException):
    def __init__(self):
        super(TokenValidationViolation, self).__init__("Given token already exists or invalid")

class ImageBase64DecodeException(TaskbeException):
    def __init__(self):
        super(ImageBase64DecodeException,self).__init__("Given image base64 string wasn't decoded successfully, "
                                                        "possibly corrupt data or invalid data format? (Note that "
                                                        "jpeg files are supported only in this version )")

class ScanNotFound(TaskbeException):
    def __init__(self):
        super(ScanNotFound, self).__init__("Given scan token not found")


class AlgorithmRequestedNotSupported(TaskbeException):
    def __init__(self):
        super(AlgorithmRequestedNotSupported, self).__init__("Algorithm requested not supported. supported algorithm "
                                                             "codes are "+str([i[0] for i in Scan.ALGORITHMS]))

