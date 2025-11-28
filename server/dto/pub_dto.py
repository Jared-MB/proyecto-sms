class PubRequestDTO:
    def __init__(self, data):
        self.IDEPUB = data.get("IDEPUB")
        self.FECPUB = data.get("FECPUB")
        self.NOMPUB = data.get("NOMPUB")
        self.NOPPUB = data.get("NOPPUB")
        self.MEDPUB = data.get("MEDPUB")
        self.CONPUB = data.get("CONPUB")
        self.DOCPUB = data.get("DOCPUB")

    def to_dict(self):
        return {
            "IDEPUB": self.IDEPUB,
            "FECPUB": self.FECPUB,
            "NOMPUB": self.NOMPUB,
            "NOPPUB": self.NOPPUB,
            "MEDPUB": self.MEDPUB,
            "CONPUB": self.CONPUB,
            "DOCPUB": self.DOCPUB
        }


class PubResponseDTO:
    def __init__(self, pub):
        self.IDEPUB = pub.IDEPUB
        self.FECPUB = pub.FECPUB
        self.NOMPUB = pub.NOMPUB
        self.NOPPUB = pub.NOPPUB
        self.MEDPUB = pub.MEDPUB
        self.CONPUB = pub.CONPUB
        self.DOCPUB = pub.DOCPUB

    def to_dict(self):
        return self.__dict__