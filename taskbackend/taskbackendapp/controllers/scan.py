




from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
import logging

from ..dao.scan import ScanDAO
from ..dto.scan import ScanDTO
from ..logging.levels import LogLevel
from ..logging.logging import LoggingLayer

class ScanController:
    logger=logging.getLogger("Class:ScanController")
    loggingLayer=LoggingLayer(logger).log
    dao:ScanDAO=ScanDAO()
    dto:ScanDTO=ScanDTO("ScanController")

    @staticmethod
    def getScans(req:HttpRequest):
        return JsonResponse({'all':'ok'})


    @staticmethod
    def addScan(req: HttpRequest):
        return JsonResponse({'all':'ok'})




