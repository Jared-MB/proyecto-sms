class NroRequestDTO:
    def __init__(self, data):
        self.IDENRO = data.get("IDENRO")
        self.NOMNRO = data.get("NOMNRO")
        self.NROCAP = data.get("NROCAP")

    def to_dict(self):
        return {
            "IDENRO": self.IDENRO,
            "NOMNRO": self.NOMNRO,
            "NROCAP": self.NROCAP
        }


class NroResponseDTO:
    def __init__(self, nro):
        self.IDENRO = nro.IDENRO
        self.NOMNRO = nro.NOMNRO
        self.NROCAP = nro.NROCAP

    def to_dict(self):
        return self.__dict__
