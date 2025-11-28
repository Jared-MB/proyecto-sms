class proRequestDTO:
    def __init__(self, data):
        self.IDEPRO = data.get("IDEPRO")
        self.DESPRO = data.get("DESPRO")
        self.RESPRO = data.get("RESPRO")
        self.FINPRO = data.get("FINPRO")

    def to_dict(self):
        return {
            "IDEPRO": self.IDEPRO,
            "DESPRO": self.DESPRO,
            "RESPRO": self.RESPRO,
            "FINPRO": self.FINPRO
        }


class proResponseDTO:
    def __init__(self, pro):
        self.IDEPRO = pro.IDEPRO
        self.DESPRO = pro.DESPRO
        self.RESPRO = pro.RESPRO
        self.FINPRO = pro.FINPRO

    def to_dict(self):
        return self.__dict__
