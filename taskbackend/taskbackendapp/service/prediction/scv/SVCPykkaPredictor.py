import pykka
import logging
import time
import numpy as np
import matplotlib.pyplot as plt
import pprint
from .integration.TDIDInterface import TDIDInterface
from sklearn import datasets
from sklearn import svm
import sys
import numpy




# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot


class SVCPykkaPredictor(pykka.ThreadingActor):
    def __init__(self):
        numpy.set_printoptions(threshold=sys.maxsize)
        self.a = TDIDInterface()
        self.logger = logging.getLogger("Predictor")
        super().__init__()
    def predict(self):
        image_data = self.a.data()
        print("image data shape" + str(image_data.shape))
        images = np.array([self.a.modelCompatible(self.a.grayScale(self.a.chop(x))) for x in image_data])
        targets = self.a.target()

        images, targets = TDIDInterface.shuffleDataset(600, images, targets)

        # pyplot.imshow(a.grayScale(a.chop(image_data[1])))
        # pyplot.imshow(a.chop(image_data[1]))
        # pyplot.show()

        print("D -> DATA" + str(images.shape))
        print("D -> TARGET" + str(targets.shape))

        clf = svm.SVC(gamma=0.001, C=100.)
        clf.fit(
            images[:-160],  # Images as arrays
            targets[:-160]  # Maligrant or benign
        )
        # print(clf.predict(images[-1].reshape(1, -1)))
        # print(clf.predict(images))
        # print(targets)

        con = self.a.confusionMatrix(
            targets[len(targets) - 160:],  # Pass the Targets
            clf.predict(images[len(targets) - 160:])  # Pass what the model predicts
        )
        print(con)
        print(con[0] / (con[0] + con[1]))
        return ("Maligrant","Mocked")
    def on_receive(self, message) :
        scan=message[0]
        callback=message[1]
        result = self.predict()
        callback(scan,result[0],result[1])

