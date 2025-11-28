class NecRequestDTO:
    def __init__(self, data):
        self.IDENEC = data.get("IDENEC")
        self.EDINEC = data.get("EDINEC")
        self.DOCNEC = data.get("DOCNEC")
        self.NECCAP = data.get("NECCAP")

    def to_dict(self):
        return {
            "IDENEC": self.IDENEC,
            "EDINEC": self.EDINEC,
            "DOCNEC": self.DOCNEC,
            "NECCAP": self.NECCAP
        }


class NecResponseDTO:
    def __init__(self, nec):
        self.IDENEC = nec.IDENEC
        self.EDINEC = nec.EDINEC
        self.DOCNEC = nec.DOCNEC
        self.NECCAP = nec.NECCAP

    def to_dict(self):
        return self.__dict__