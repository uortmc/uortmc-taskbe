import pykka
from PIL import Image
import io
from ..AbstractPredictor import AbstractPredictor
from ....models import Scan
import numpy
import base64



# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot


class RasNetPykkaPredictor(pykka.ThreadingActor,AbstractPredictor):
    def __init__(self):
        super().__init__()

    def loggingWithScan(self,scan:Scan,message:str):
        msg="Scan token " + str(scan.token) +"\t\t\t"+str(message)
        self.logger.error(msg)
        self.logbuffer+=msg+"\n"


    def algorithmCode(self):return "SVC"

    def decodeImage(self,base64Image: str) -> numpy.ndarray:
        image = base64.b64decode(str(base64Image))
        img = Image.open(io.BytesIO(image))
        return numpy.array(img)


    def predict(self,scan:Scan):
        return ("Benign","RasNet selector works")

    def on_receive(self, message) :
        scan=message[0]
        callback=message[1]
        result = self.predict(scan)
        callback(scan,result[0],result[1])

