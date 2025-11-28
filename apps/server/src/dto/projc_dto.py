class projcRequestDTO:
    def __init__(self, data):
        self.IDEPRO = data.get("IDEPRO")
        self.DESPRO = data.get("DESPRO")
        self.TIEPRO = data.get("TIEPRO")
        self.ESTPRO = data.get("ESTPRO")
        self.RESPRO = data.get("RESPRO")
        self.TEMPRO = data.get("TEMPRO")

    def to_dict(self):
        return {
            "IDEPRO": self.IDEPRO,
            "DESPRO": self.DESPRO,
            "TIEPRO": self.TIEPRO,
            "ESTPRO": self.ESTPRO,
            "RESPRO": self.RESPRO,
            "TEMPRO": self.TEMPRO
        }


class projcResponseDTO:
    def __init__(self, projc):
        self.IDEPRO = projc.IDEPRO
        self.DESPRO = projc.DESPRO
        self.TIEPRO = projc.TIEPRO
        self.ESTPRO = projc.ESTPRO
        self.RESPRO = projc.RESPRO
        self.TEMPRO = projc.TEMPRO

    def to_dict(self):
        return self.__dict__
