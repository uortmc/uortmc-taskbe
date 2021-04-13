




from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
import logging

from ..dao.scan import ScanDAO
from ..dto.scan import ScanDTO
from ..exceptions.base import FieldsMissingException
from ..exceptions.scan import TokenValidationViolation, ScanNotFound, ImageBase64DecodeException
from ..logging.levels import LogLevel
from ..logging.logging import LoggingLayer
from ..models import Scan
from ..service.InfoBeService import InfoBeService


class ScanController:
    logger=logging.getLogger("Class:ScanController")
    loggingLayer=LoggingLayer(logger).log
    dao:ScanDAO=ScanDAO()
    dto:ScanDTO=ScanDTO("ScanController")
    infoBeService:InfoBeService=InfoBeService()

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
            (token,image)=ScanController.__getFieldsFromAddRequest(req)
            image=ScanController.__validateBase64Image(image)
            scan:Scan=ScanController.dao.addScan(token,image)
            mocked=ScanController.infoBeService.proccessScan(scan)
            return JsonResponse(
                ScanController.loggingLayer(
                    ScanController.dto.successAddScan(scan)
                )
            )
        except (TokenValidationViolation,FieldsMissingException,ImageBase64DecodeException) as e:
            return JsonResponse(
                ScanController.loggingLayer(
                    ScanController.dto.fail(e.reason),LogLevel.ERROR
                )
            )

    @staticmethod
    def __getFieldsFromAddRequest(req:HttpRequest)->():
        try:
            return (req.POST['token'],req.POST['image'])
        except MultiValueDictKeyError:
            raise FieldsMissingException

    @staticmethod
    def __validateBase64Image(base64:str)->str:
        raise ImageBase64DecodeException()
        #return base64

    @staticmethod
    def __getTokenFromGetRequest(req: HttpRequest) -> str:
        try:
            return req.GET['token']
        except MultiValueDictKeyError:
            raise FieldsMissingException





