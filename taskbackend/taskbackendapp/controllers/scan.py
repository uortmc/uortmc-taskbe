




from django.db import IntegrityError
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
import logging
import base64
import imghdr
from ..dao.scan import ScanDAO
from ..dto.scan import ScanDTO
from ..exceptions.base import FieldsMissingException
from ..exceptions.scan import TokenValidationViolation, ScanNotFound, ImageBase64DecodeException
from ..logging.levels import LogLevel
from ..logging.logging import LoggingLayer
from ..models import Scan
from ..service.coms.InfobackendService import InfobackendService
from ..service.prediction.PredictionService import PredictionService



class ScanController:
    logger=logging.getLogger("Class:ScanController")
    loggingLayer=LoggingLayer(logger).log
    dao:ScanDAO=ScanDAO()
    dto:ScanDTO=ScanDTO("ScanController")
    infoBackendService:InfobackendService=InfobackendService()
    predictionService:PredictionService=PredictionService(dao,infoBackendService)


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
            mocked=ScanController.predictionService.proccessScan(scan)
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
    def __validateBase64Image(base64Img:str)->str:
        """
            The tests list returns the list of the checks to be made for a specific file format. tests[1] checks if the
            underlying image is a png image.
        """
        try:
            if(not imghdr.tests[1](base64.b64decode(base64Img),None) == 'png'):
                raise ImageBase64DecodeException()
        except:
            raise ImageBase64DecodeException()
        return base64Img

    @staticmethod
    def __getTokenFromGetRequest(req: HttpRequest) -> str:
        try:
            return req.GET['token']
        except MultiValueDictKeyError:
            raise FieldsMissingException





