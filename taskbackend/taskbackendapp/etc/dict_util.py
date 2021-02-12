class DictUtils:
    @staticmethod
    def merge(a:dict,b:dict)->dict:
        retval = a.copy()
        retval.update(b)
        return retval