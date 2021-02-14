import requests

from ..enviroment import Enviroment
from ..models import Scan

import logging
class InfoBeService:

    def proccessScan(self,scan:Scan):
        return self.declareTaskComplete(scan)

    def declareTaskComplete(self,scan:Scan):

        url = Enviroment.SCANCOMPLETE_URL
        payload = 'token='+scan.token
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response


