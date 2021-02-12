from ..etc.dict_util import DictUtils

class AbstractDTO:
    def __init__(self,handlerName:str):
        self.handlerName=handlerName

    def status(self,status: bool) -> dict:
        return {
            "complete": status,
            "handler":self.handlerName
        }
    def fail(self,reason:str):
        return DictUtils.merge(
                self.status(False),
                {'reason':reason})

    def success(self):
        return self.status(True)

    def successWithResponce(self,responce):
        return DictUtils.merge(self.success(),
                    {"responce":responce})
