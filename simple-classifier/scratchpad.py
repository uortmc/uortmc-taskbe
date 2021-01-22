
import matplotlib.pyplot as pyplot

from integration.TDIDInterface import TDIDInterface
from integration.DDITInterface import DDITInterface

a=TDIDInterface()
b=DDITInterface()

a_data=a.data()
a_target=a.target()
b_data=b.data()
b_target=b.target()
print(a_target.shape)
print(b_target.shape)
