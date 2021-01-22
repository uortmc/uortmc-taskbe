from matplotlib import image
from matplotlib import pyplot
import numpy as np


"""
This is a interface to our infrastructure, of what a 'dataset' means.
"""
class CompatibleDataset:
    """
        Return an array of both maligrant and benign cases as 2D normalized np.array
    """
    def data(self):
        pass
    """
        Return an array of the targets. for a given self.data()[i] , the self.target()[i] will return its label
        0 for benign, 1 for maligrant, for now
    """
    def target(self):
        pass

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


#stats
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


