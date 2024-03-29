from django.db import IntegrityError

from ..exceptions.scan import TokenValidationViolation, ScanNotFound
from ..models import Scan


class ScanDAO:
    def addScan(self,token,image,algorithm:str):
        try:
            s=Scan(token=token,image=image,algorithm=algorithm)
            s.save()
            return s
        except IntegrityError as e:
            raise TokenValidationViolation


    def getScan(self,token):
        s = Scan.objects.filter(token=token)
        if (len(s)==0):
            raise ScanNotFound
        return s[0]  # Token is unique, so this list will always have 1 or 0 elements

    def scanCompleted(self,scan:Scan,prediction:str,results:str)->Scan:
        scan.prediction = prediction
        scan.results = results
        scan.save()
        return scan


