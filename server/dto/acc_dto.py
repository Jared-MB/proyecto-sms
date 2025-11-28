class accRequestDTO:
    def __init__(self, data):
        self.IDEACC = data.get("IDEACC")
        self.DESACC = data.get("DESACC")
        self.RESACC = data.get("RESACC")
        self.FECACC = data.get("FECACC")

    def to_dict(self):
        return {
            "IDEACC": self.IDEACC,
            "DESACC": self.DESACC,
            "RESACC": self.RESACC,
            "FECACC": self.FECACC
        }


class accResponseDTO:
    def __init__(self, acc):
        self.IDEACC = acc.IDEACC
        self.DESACC = acc.DESACC
        self.RESACC = acc.RESACC
        self.FECACC = acc.FECACC

    def to_dict(self):
        return self.__dict__
