from ..models import Scan


class ScanSerializer():
    @staticmethod
    def toDict(scan:Scan)->dict:
        return {
            "algorithm":scan.algorithm,
            "token":scan.token,
            "image":scan.image,
            "results":scan.results,
            "prediction":scan.prediction
        }
