from matplotlib import image
from matplotlib import pyplot
import numpy as np

from filters.Chop import Chop
from filters.Grayscale import Grayscale
from random import randint
"""
This is a interface to our infrastructure, of what a 'dataset' means.
"""
class CompatibleDataset:
    """
        Return an array of both malignant and benign cases as 2D normalized np.array
    """
    def data(self):
        pass
    """
        Return an array of the targets. for a given self.data()[i] , the self.target()[i] will return its label
        0 for benign, 1 for malignant, for now
    """
    def target(self):
        pass

    """
        A simple method that converts the TIRADS dataset into a binary Malignant-Benign dataset. 
    
    """
    @staticmethod
    def tiradsToTarget(tirads):
        if (tirads == "2" or tirads == "3"):
            return 0
        else:
            return 1

    """
        Converts a 2D array into a single array. this is compatible with skit-learn
        Please apply this function only after your appled filters.
    """
    def modelCompatible(self, image):
        return image.flatten()

#=================================================================================== Image filters
    """
        Chops the scans and returns the exact data area
    """

    def chop(self, image):
        return Chop.apply(image, 139, 145, 5, 50)

    """
        A simple spartial domain filter to convert the image into grayscale
    """

    def grayScale(self, image):
        return Grayscale.apply(image)


#=================================================================================== Stats
    def confusionMatrix(self,target,estimated):
        positive=negative=positive_negative=negative_positive=0
        assert target.shape==estimated.shape

        for i in range(len(target)):
            if(target[i]==estimated[i]):
                positive+=1
            if (target[i] != estimated[i]):
                negative += 1
            if (target[i] == 1 and estimated[i] == 0):
                negative_positive += 1
            if (target[i] == 0 and estimated[i] == 1):
                positive_negative += 1
        return [positive,negative,positive_negative,negative_positive]

#=================================================================================== Shuffle
    """
    Assuming that data will be a array of shape (n,84180)
    
    """
    @staticmethod
    def shuffleDataset(iterations,data,targets)->tuple:
        dataShape=data.shape
        dataPoints=dataShape[0]
        assert dataPoints==targets.shape[0]  #Just a check to verify that there is equal amount of datapoints and targets
        swapPositiona=swapPositionb=None
        dataa=datab=targeta=targetb=None
        for i in range(iterations):
            swapPositiona,swapPositionb=randint(0,dataPoints-1),randint(0,dataPoints-1)
            if swapPositionb==swapPositiona:continue
            dataa=data[swapPositiona]
            targeta=targets[swapPositiona]
            datab = data[swapPositionb]
            targetb = targets[swapPositionb]

            data[swapPositiona]=datab
            targets[swapPositiona]=targetb

            data[swapPositionb] = dataa
            targets[swapPositionb] = targeta

        return data,targets





