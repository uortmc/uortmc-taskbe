import xmltodict

from matplotlib import image
from matplotlib import pyplot
import numpy as np
from .CompatibleDataset import CompatibleDataset

"""
This is a interface to our infrastructure, of what a 'dataset' means.
"""
class TDIDInterface(CompatibleDataset):
    xmlroot = "../data/tdid/xml/"
    rawjpgroot = "../data/tdid/raw_jpg/"

    images=list()
    targets=list()
    notfound=list()
    def imageFilename(self,number):
        return self.rawjpgroot + str(number) + "_1.jpg"

    def xmlFilename(self, number):
        return self.xmlroot +str(number) + ".xml"

    def __init__(self):
        for i in range(1, 400): #make this dynamic, handcoded values are not good :P
            try:
                curr_xml = open(self.xmlFilename(i)).read()
                curr_image = image.imread(self.imageFilename(i))
                curr_xml_parsed = xmltodict.parse(curr_xml)
                curr_label=CompatibleDataset.tiradsToTarget(curr_xml_parsed['case']['tirads'])
                self.targets.append(curr_label)
                self.images.append(curr_image)

            except FileNotFoundError:
                self.notfound.append(i)

        print("Image load complete, but images "+str(self.notfound)+" not found")

    def data(self):
        return np.array(self.images)

    def target(self):
        return np.array(self.targets)







