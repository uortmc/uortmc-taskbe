import base64
from PIL import Image
import io
import numpy


def decodeImage(base64Image:str)->numpy.ndarray:
    image = base64.b64decode(str(base64Image))
    img = Image.open(io.BytesIO(image))
    return numpy.array(img)