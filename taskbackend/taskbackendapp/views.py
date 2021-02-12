from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .controllers.scan import ScanController

def addScan(req):
    return ScanController.addScan(req)
def getScan(req):
    return ScanController.getScans(req)

