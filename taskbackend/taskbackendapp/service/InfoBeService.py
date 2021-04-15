import requests

from .scv.SCVPredictor import SCVPredictor
from ..enviroment import Enviroment
from ..models import Scan

import logging
class InfoBeService:
    def __init__(self):
        self.scvPredictor=SCVPredictor.start()

    def proccessScan(self,scan:Scan):
        self.scvPredictor.tell((scan,lambda scan,results,output:self.declareTaskComplete(scan,results,output)))

    def declareTaskComplete(self,scan:Scan,prediction:str,algorithmOutput:str):
        """
            1) sent request
            2) call dao and update result and output
            3) end-to-end-testing

        """
        url = Enviroment.SCANCOMPLETE_URL
        #payload = 'token='+scan.token

        payload={
            'token':scan.token,
            'prediction':prediction,
            'algorithmOutput':algorithmOutput
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response


