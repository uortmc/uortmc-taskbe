import requests

from ..models import Scan


class InfoBeService:

    def  proccessScan(self,scan:Scan):
        return self.declareTaskComplete(scan)

    def declareTaskComplete(self,scan:Scan):

        url = "http://127.0.0.1:3001/app/scancomplete"

        payload = scan.token
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'sessionid=5oxjt796w9s6xo3g6kjimzsvgk5uycih'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

