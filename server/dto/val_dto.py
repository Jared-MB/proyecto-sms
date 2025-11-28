class valRequestDTO:
    def __init__(self, data):
        self.IDEVAL = data.get("IDEVAL")
        self.PERVAL = data.get("PERVAL")
        self.DIAVAL = data.get("DIAVAL")
        self.HORINI = data.get("HORINI")
        self.FECVAL = data.get("FECVAL")
        self.CALVAL = data.get("CALVAL")
        self.DIAEXT = data.get("DIAEXT")

    def to_dict(self):
        return {
            "IDEVAL": self.IDEVAL,
            "PERVAL": self.PERVAL,
            "DIAVAL": self.DIAVAL,
            "HORINI": self.HORINI,
            "FECVAL": self.FECVAL,
            "CALVAL": self.CALVAL,
            "DIAEXT": self.DIAEXT
        }


class valResponseDTO:
    def __init__(self, val):
        self.IDEVAL = val.IDEVAL
        self.PERVAL = val.PERVAL
        self.DIAVAL = val.DIAVAL
        self.HORINI = val.HORINI
        self.FECVAL = val.FECVAL
        self.CALVAL = val.CALVAL
        self.DIAEXT = val.DIAEXT

    def to_dict(self):
        return self.__dict__
