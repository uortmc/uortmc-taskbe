
import numpy as np
class Chop:
    @staticmethod
    def apply(image,zero_x,x_max,zero_y,y_max):
        retval = image
        retval = np.delete(retval, [x for x in range(zero_x)], 1)  # chopped left
        retval = np.delete(retval, [-x for x in range(x_max)], 1)  # chopped right
        retval = np.delete(retval, [x for x in range(zero_y)], 0)  # chopped up
        retval = np.delete(retval, [-x for x in range(y_max)], 0)  # chopped down
        return retval
