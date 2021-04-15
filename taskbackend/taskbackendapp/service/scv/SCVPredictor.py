import pykka
import logging
class SCVPredictor(pykka.ThreadingActor):
    def __init__(self):
        self.a = logging.getLogger("Predictor")
        super().__init__()
    def on_receive(self, message) :
        scan=message[0]
        callback=message[1]
        callback(scan,"Maligrant","Mocked")
        logging.error("pykka responds")

