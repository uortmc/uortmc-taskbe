
class TaskbeException(BaseException):
    def __init__(self,reason):
        self.reason=reason

    def getReason(self):
        return self.reason

class FieldsMissingException(TaskbeException):
    def __init__(self):
        super(FieldsMissingException,self).__init__("Bad request: Request without the necessary fields has being "
                                                    "raised.")
