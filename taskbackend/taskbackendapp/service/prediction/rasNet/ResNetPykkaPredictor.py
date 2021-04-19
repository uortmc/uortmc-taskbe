import pykka
from PIL import Image
import io
from ..AbstractPredictor import AbstractPredictor
from ....models import Scan
import numpy
import base64
import torch
from .ResNet import ResNet

from PIL import Image
import torchvision.transforms as transforms
import logging


# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot


class ResNetPykkaPredictor(pykka.ThreadingActor, AbstractPredictor):
    def __init__(self):
        # if GPU is available, use GPU; otherwise use CPU
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        # functions for loading image
        self.image_transformer = transforms.Compose([
            transforms.Grayscale(),
            transforms.ToTensor(),
            transforms.Normalize(0.5, 0.5)
        ])
        self.model = ResNet(label_size=2)
        self.model.load_state_dict(torch.load(f'resnet18.tch', map_location=torch.device('cpu')))
        self.model.eval()
        self.model = self.model.to(self.device)
        self.logger = logging.getLogger("RasNetPykkaPredictor")
        self.logger.setLevel(logging.NOTSET)
        self.logbuffer = ""
        super().__init__()

    def loggingWithScan(self,scan:Scan,message:str):
        msg="Scan token " + str(scan.token) +"\t\t\t"+str(message)
        self.logger.error(msg)
        self.logbuffer+=msg+"\n"

    def decodeImage(self,base64Image: str):
        image = base64.b64decode(str(base64Image))
        img = Image.open(io.BytesIO(image))
        return img

    def algorithmCode(self):return "RES"


    def predict(self,scan:Scan):
        try:
            img=self.image_transformer(self.decodeImage(scan.image))
            img = transforms.functional.crop(img, 8, 87, 301, 385)
            self.loggingWithScan(scan,"RASNET Algorithm initialized")
            prediction = self.model(img).argmax().item()
            self.loggingWithScan(scan, "Model predicted: "+str(prediction))
            if prediction == 0:
                return ("Benign","Operation completed")
            elif prediction == 1:
                return ("Malignant", "Operation completed")
        except Exception as e:
            msg="Operation failed due to "+str(e)
            self.loggingWithScan(scan, msg)
            return ("Not Set",msg)

    def on_receive(self, message):
        scan=message[0]
        callback=message[1]
        result = self.predict(scan)
        callback(scan,result[0],result[1])

