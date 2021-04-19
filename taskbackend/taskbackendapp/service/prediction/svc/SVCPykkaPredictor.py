import pykka
import logging
import time
import numpy as np
import matplotlib.pyplot as plt
import pprint
import base64
from PIL import Image
import io
import numpy

from ..AbstractPredictor import AbstractPredictor
from ....models import Scan
from .integration.TDIDInterface import TDIDInterface
from sklearn import datasets
from sklearn import svm
import sys
import numpy
import base64



# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot


class SVCPykkaPredictor(pykka.ThreadingActor,AbstractPredictor):
    def __init__(self):
        numpy.set_printoptions(threshold=sys.maxsize)
        self.a = TDIDInterface()
        self.logger = logging.getLogger("SVCPykkaPredictor")
        self.logger.setLevel(logging.NOTSET)
        self.logbuffer=""
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
        try:
            self.loggingWithScan(scan,"Proccess initialization start")
            image_data = self.a.data()
            self.loggingWithScan(scan, str(image_data.shape) + " Healty datapoints loaded into memory")
            images = np.array([self.a.modelCompatible(self.a.grayScale(self.a.chop(x))) for x in image_data])
            self.loggingWithScan(scan, "Grayscale and chop filters applied successfuly")
            targets = self.a.target()
            self.loggingWithScan(scan, str(targets.shape) + " healty targets loaded into memory")
            images, targets = TDIDInterface.shuffleDataset(600, images, targets)
            self.loggingWithScan(scan, "shuffling with 600 passes completed")
            # pyplot.imshow(a.grayScale(a.chop(image_data[1])))
            # pyplot.imshow(a.chop(image_data[1]))
            # pyplot.show()
            clf = svm.SVC(gamma=0.001, C=100.)
            self.loggingWithScan(scan, "Support Vector Machine loaded into memory")
            clf.fit(
                images[:-160],  # Images as arrays
                targets[:-160]  # Maligrant or benign
            )
            self.loggingWithScan(scan, "Fitting completed")

            # print(clf.predict(images[-1].reshape(1, -1)))
            # print(clf.predict(images))
            # print(targets)

            con = self.a.confusionMatrix(
                targets[len(targets) - 160:],  # Pass the Targets
                clf.predict(images[len(targets) - 160:])  # Pass what the model predicts
            )
            self.loggingWithScan(scan, "confusionMatrix:" + str(con))
            self.loggingWithScan(scan, "Model Success Rate : " + str(con[0] / (con[0] + con[1])))

            decodedImage=self.decodeImage(scan.image)
            self.loggingWithScan(scan, "Scan image loaded : "+str(decodedImage.shape))
            decodedImage=self.a.grayScale(self.a.chop(decodedImage))
            self.loggingWithScan(scan, "Filters Applied" + str(decodedImage.shape))
            #Apply filter, ensure that this shit works
            self.loggingWithScan(scan,clf.predict(decodedImage.reshape(1, -1)))
            result=clf.predict(decodedImage.reshape(1, -1))[0]
            if(result==1):result="Malignant"
            else:result="Benign"
            algorithmResult=self.logbuffer
            self.logbuffer=""
            return (result, algorithmResult)
        except BaseException as e:
            self.logger.error(e.__str__())
            return ("Not Set","Operation failed due to "+str(e))

    def on_receive(self, message) :
        scan=message[0]
        callback=message[1]
        result = self.predict(scan)
        callback(scan,result[0],result[1])

