from ..dto.abstract import AbstractDTO
from ..models import Scan
from ..serializers.scan import ScanSerializer


class ScanDTO(AbstractDTO):
    def __init__(self,handler):
        super(ScanDTO, self).__init__(handler)
        self.handler=handler

    def successAddScan(self,s:Scan):
        return self.successScanOperation(s)
    def successGetScan(self,s:Scan):
        return self.successScanOperation(s)
    def successScanOperation(self, s:Scan):
        return self.successWithResponce(
            ScanSerializer.toDict(s)
        )

