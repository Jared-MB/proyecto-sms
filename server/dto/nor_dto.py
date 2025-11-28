class NorRequestDTO:
    def __init__(self, data):
        self.IDENOR = data.get("IDENOR")
        self.NOMNOR = data.get("NOMNOR")
        self.NORTPO = data.get("NORTPO")

    def to_dict(self):
        return {
            "IDENOR": self.IDENOR,
            "NOMNOR": self.NOMNOR,
            "NORTPO": self.NORTPO
        }


class NorResponseDTO:
    def __init__(self, nor):
        self.IDENOR = nor.IDENOR
        self.NOMNOR = nor.NOMNOR
        self.NORTPO = nor.NORTPO

    def to_dict(self):
        return self.__dict__
