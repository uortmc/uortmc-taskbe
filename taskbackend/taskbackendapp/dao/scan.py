from django.db import IntegrityError

from ..exceptions.scan import TokenValidationViolation, ScanNotFound
from ..models import Scan


class ScanDAO:
    def addScan(self,token):
        try:
            s=Scan(token=token)
            s.save()
            return s
        except IntegrityError as e:
            raise TokenValidationViolation
    def getScan(self,token):
        s = Scan.objects.filter(token=token)
        if (len(s)==0):
            raise ScanNotFound
        return s[0]  # Token is unique, so this list will always have 1 or 0 elements


