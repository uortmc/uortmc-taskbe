import numpy as np
import matplotlib.pyplot as plt
import pprint
from integration.TDIDInterface import TDIDInterface
from sklearn import datasets
from sklearn import svm
import sys
import numpy


numpy.set_printoptions(threshold=sys.maxsize)
a = TDIDInterface()

# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot


image_data = a.data()
print("image data shape"+str(image_data.shape))
images = np.array([a.modelCompatible(a.grayScale(a.chop(x))) for x in image_data])
targets = a.target()

images,targets=TDIDInterface.shuffleDataset(600,images,targets)

#pyplot.imshow(a.grayScale(a.chop(image_data[1])))
#pyplot.imshow(a.chop(image_data[1]))
#pyplot.show()


print("D -> DATA"+str(images.shape))
print("D -> TARGET"+str(targets.shape))

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(
    images[:-160],                                              #Images as arrays
    targets[:-160]                                              #Maligrant or benign
)
#print(clf.predict(images[-1].reshape(1, -1)))
#print(clf.predict(images))
#print(targets)

con=a.confusionMatrix(
    targets[len(targets)-160:],                             #Pass the Targets
    clf.predict(images[len(targets)-160:])                  #Pass what the model predicts
)
print(con)
print(con[0]/(con[0]+con[1]))




