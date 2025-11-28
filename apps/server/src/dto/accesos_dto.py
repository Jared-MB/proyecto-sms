class AccesosRequestDTO:
    def __init__(self, data):
        self.ideacc = data.get("ideacc")
        self.diracc = data.get("diracc")
        self.fecacc = data.get("fecacc")
        self.broacc = data.get("broacc")
        self.useacc = data.get("useacc")

    def to_dict(self):
        return {
            "ideacc": self.ideacc,
            "diracc": self.diracc,
            "fecacc": self.fecacc,
            "broacc": self.broacc,
            "useacc": self.useacc
        }


class AccesosResponseDTO:
    def __init__(self, acc):
        self.ideacc = acc.IDEACC
        self.diracc = acc.DIRACC
        self.fecacc = acc.FECACC
        self.broacc = acc.BROACC
        self.useacc = acc.USEACC

    def to_dict(self):
        return self.__dict__
