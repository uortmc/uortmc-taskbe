import requests

from .rasNet.ResNetPykkaPredictor import ResNetPykkaPredictor
from .svc.SVCPykkaPredictor import SVCPykkaPredictor
from ...dao.scan import ScanDAO
from ...models import Scan
from ..coms import InfobackendService
import logging


class PredictionService:
    def __init__(self, scanDao: ScanDAO, infobackendService: InfobackendService):
        self.scvPredictor = SVCPykkaPredictor.start()
        self.resNetPredictor = ResNetPykkaPredictor.start()
        self.scanDAO = scanDao
        self.infobackendService = infobackendService


    def proccessScan(self, scan: Scan):
        if(scan.algorithm=='SVC'):
            self.scvPredictor.tell(
                (scan,lambda scan, results, output:
                    self.declareScanComplete(scan, results, output)))
        elif(scan.algorithm=='RES'):
            self.resNetPredictor.tell(
                (scan,lambda scan, results, output:
                    self.declareScanComplete(scan, results, output))
            )
        else:
            self.declareScanComplete(
                scan,
                prediction="Operation Failed",
                algorithmOutput="Selected algorithm not supported"
            )

    def declareScanComplete(self, scan: Scan, prediction: str, algorithmOutput: str):
        self.scanDAO.scanCompleted(scan, prediction, algorithmOutput)
        self.infobackendService.sentTaskCompleteNotification(scan)
