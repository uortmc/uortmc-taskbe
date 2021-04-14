# uortmc-taskbe

This microservice will have the responsibility to perform predictions on a given scan, and return its results
on the frontend.

In order to run ...
1. Duplicate .env.local
2. Rename to .env
3. run
```shell script
  source .env     
  heroku local

```
```
.env must be renamed and sourced, because heroku local depends on PORT enviromental variable to select the port to bind
.env is a typical KEY=VALUE format, with 'export's included. thore are ignored by the library, makes possible to source and 
load the same file. 
  
```
### Simple Classifier
Simple Classifier is as the name suggests, a simple classification(A support vector machine) method with all its required integrations
and supported code. it features a clean and modular architecture that enables the plug-and-play of various
image filters(Only 2 are supported currently though, Grayscale and Chop).

#### Dataset Integration   

Special care has been given in the architecture of this solution. In a result of this, an arbitary dataset can be included to the solution
with minimal effort. The only thing that needs to be done, is to extend the CompatibleDataset interface

```python

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
```
There are currently 1 dataset implementation, [TDID](http://cimalab.intec.co/?lang=en&mod=program&id=5)

#### Filters

2 Very simple spatial-domain filters are given, Chop and Grayscale on the respective classes. The plugin of different 
filters is very easy process. In the following code, two of the filters are applied

```python
import numpy as np
import matplotlib.pyplot as plt
import pprint
from integration.TDIDInterface import TDIDInterface
from sklearn import datasets
from sklearn import svm
import sys
import numpy

a = TDIDInterface()

image_data = a.data()
targets = a.target()

image_data = np.array([a.modelCompatible(a.grayScale(a.chop(x))) for x in image_data])
```

Dont forget to call .modelCompatible, as internally, a datapoint is a list 84180 elements (all images are 360x560=84180)

