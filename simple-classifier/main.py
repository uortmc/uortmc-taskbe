import numpy as np
import matplotlib.pyplot as plt
import pprint
from integration.TDIDInterface import TDIDInterface
from integration.DDITInterface import DDITInterface
from sklearn import datasets
from sklearn import svm
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
a = TDIDInterface()
digits = datasets.load_digits()
# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot


image_data = a.data()
images = np.array([a.modelCompatible(a.grayScale(a.chop(x))) for x in image_data])

targets = a.target()
#pyplot.imshow(a.grayScale(a.chop(image_data[1])))
#pyplot.imshow(a.chop(image_data[1]))
#pyplot.show()


print("D -> DATA"+str(digits.data.shape))
print("D -> TARGET"+str(digits.target.shape))
print("D -> DATA"+str(images.shape))
print("D -> TARGET"+str(targets.shape))

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(images[:-160], targets[:-160])
#print(clf.predict(images[-1].reshape(1, -1)))
#print(clf.predict(images))
#print(targets)
print(a.confusionMatrix(targets[len(targets)-160:],clf.predict(images[len(targets)-160:])))


