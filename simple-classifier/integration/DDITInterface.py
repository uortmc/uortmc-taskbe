from matplotlib import image
from matplotlib import pyplot
import numpy as np
from integration.CompatibleDataset import CompatibleDataset
from filters.Chop import Chop
from filters.Grayscale import Grayscale
"""
A class that converts the DDIT dataset into scikit-lean compatible data points
"""
class DDITInterface(CompatibleDataset):
    dbroot= "../data/ddti/thyroid"
    malignsRoot = "../data/ddti/maling"
    benignsRoot = "../data/ddti/bening"

    #This is used to filter out everything thats not valid (noisy images etc)
    maligrantCases = [6 , 7 , 9 , 12 , 15 , 17 , 22 , 24 , 25 , 42 , 44 , 48 , 50 , 51 , 52 , 63 , 75 , 77 , 80 , 89 , 1 , 11 , 14 , 16 , 19 , 28 , 38 , 53 , 57 , 58 , 59 , 62 , 83 , 92 , 97 , 99 , 4 , 18 , 29 , 31 , 33 , 34 , 35 , 46 , 66 , 70 , 71 , 74 , 76 , 87 , 88 , 94 , 95 , 96 , 98 , 13 , 23 , 32 , 36 , 54 , 60 , 61 , 64 , 67 , 78 , 90 ]
    benignsCases=[2 , 3 , 10 , 21 , 27 , 30  , 41 , 43 , 45 , 49 , 55 , 56 , 65 , 68 , 72 , 73 , 82 , 84 , 85 , 86 , 93 , 5 , 8 , 20 , 26 , 39 , 40 , 47 , 69 , 79 , 81 , 91 ]
    def __init__(self) -> None:
        super().__init__()

    def filename(self,number,root):
        return root + "/" + str(number) + "_1.jpg"
    """
    load(number)
        Loads a specific image, the number is the image number
    """
    def load(self,number):
        return image.imread(self.filename(number,DDITInterface.dbroot))
    """
        Loads a malign image, returns a np.array
    """
    def loadMalign(self, number):
        return np.array(image.imread(self.filename(DDITInterface.maligrantCases[number],DDITInterface.dbroot)))

    """
        Loads a benign image, returns a np.array
    """
    def loadBenign(self, number):
        return np.array(image.imread(self.filename(DDITInterface.benignsCases[number],DDITInterface.dbroot)))
    """
        Load all Malign cases, return as 2D np.array
    """
    def loadAllMaligrant(self):
        print("LOAD "+str(len(DDITInterface.maligrantCases))+": Maligrant Cases")
        return np.array([self.loadMalign(x) for x in range(len(DDITInterface.maligrantCases))])
    """
        Load all Benign cases, return as 2D np.array
    """
    def loadAllBenigns(self):
        print("LOAD " + str(len(DDITInterface.benignsCases)) + ": Benigns Cases")
        return np.array([self.loadBenign(x) for x in range(len(DDITInterface.benignsCases))])
    """
        Return an array of both maligrant and benign cases 
    """
    def data(self):
        return np.append(np.array(self.loadAllMaligrant()),np.array(self.loadAllBenigns()),axis=0)
    """
        Return an array of the targets. for a given self.data()[i] , the self.target()[i] will return its label
    """
    def target(self):
        return np.array([1 for x in range(len(DDITInterface.maligrantCases))] + [0 for x in range(len(DDITInterface.benignsCases))])


    #image filters
    """
        Chops the scans and returns the exact data area
    """
    def chop(self,image):
        return Chop.apply(image,139,145,5,50)
    """
        A simple spartial domain filter to convert the image into grayscale
    """
    def grayScale(self,image):
        return Grayscale.apply(image)








