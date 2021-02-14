import os
class Enviroment:
    INFOBACKEND_URL=os.environ['INFOBACKEND_URL']
    SCANCOMPLETE_URL=INFOBACKEND_URL+"/app/scancomplete"