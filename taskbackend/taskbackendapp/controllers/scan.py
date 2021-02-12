




from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
import logging

from ..dao.scan import ScanDAO
from ..dto.scan import ScanDTO
from ..exceptions.base import FieldsMissingException
from ..exceptions.scan import TokenValidationViolation, ScanNotFound
from ..logging.levels import LogLevel
from ..logging.logging import LoggingLayer
from ..models import Scan


class ScanController:
    logger=logging.getLogger("Class:ScanController")
    loggingLayer=LoggingLayer(logger).log
    dao:ScanDAO=ScanDAO()
    dto:ScanDTO=ScanDTO("ScanController")

    @staticmethod
    def getScans(req:HttpRequest):
        try:
            token=ScanController.__getTokenFromGetRequest(req)
            scan:Scan=ScanController.dao.getScan(token)
            return JsonResponse(
                ScanController.loggingLayer(
                    ScanController.dto.successGetScan(scan)
                )
            )
        except (ScanNotFound,FieldsMissingException) as e:
            return JsonResponse(
                ScanController.loggingLayer(
                    ScanController.dto.fail(e.reason),LogLevel.ERROR
                )
            )



    @staticmethod
    def addScan(req: HttpRequest):
        try:
            token=ScanController.__getTokenFromAddRequest(req)
            scan:Scan=ScanController.dao.addScan(token)
            return JsonResponse(
                ScanController.loggingLayer(
                    ScanController.dto.successAddScan(scan)
                )
            )
        except (TokenValidationViolation,FieldsMissingException) as e:
            return JsonResponse(
                ScanController.loggingLayer(
                    ScanController.dto.fail(e.reason),LogLevel.ERROR
                )
            )

    @staticmethod
    def __getTokenFromAddRequest(req:HttpRequest)->str:
        try:
            return req.POST['token']
        except MultiValueDictKeyError:
            raise FieldsMissingException

    @staticmethod
    def __getTokenFromGetRequest(req: HttpRequest) -> str:
        try:
            return req.GET['token']
        except MultiValueDictKeyError:
            raise FieldsMissingException





