import requests

from .scv.SCVPredictor import SCVPredictor
from ...dao.scan import ScanDAO
from ...models import Scan
from ..coms import InfobackendService
import logging


class PredictionService:
    def __init__(self, scanDao: ScanDAO, infobackendService: InfobackendService):
        self.scvPredictor = SCVPredictor.start()
        self.scanDAO = scanDao
        self.infobackendService = infobackendService

    def proccessScan(self, scan: Scan):
        self.scvPredictor.tell((scan, lambda scan, results, output: self.declareScanComplete(scan, results, output)))

    def declareScanComplete(self, scan: Scan, prediction: str, algorithmOutput: str):
        self.scanDAO.scanCompleted(scan, prediction, algorithmOutput)
        self.infobackendService.sentTaskCompleteNotification(scan)
