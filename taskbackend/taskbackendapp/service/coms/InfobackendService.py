
from ...enviroment import Enviroment
import requests
from ...models import Scan


class InfobackendService():
    def __init__(self):
        pass

    def sentTaskCompleteNotification(self, scan: Scan):
        url = Enviroment.SCANCOMPLETE_URL
        payload = {'token': scan.token}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

