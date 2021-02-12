from django.urls import path

from . import views

urlpatterns = [
    path('scan/addscan', views.addScan, name='addscan'),
    path('scan/getscan', views.getScan, name='getscan')
]