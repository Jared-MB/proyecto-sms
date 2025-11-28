class TenRequestDTO:
    def __init__(self, data):
        self.IDETEN = data.get("IDETEN")
        self.NOMTEN = data.get("NOMTEN")
        self.INCTEN = data.get("INCTEN")

    def to_dict(self):
        return {
            "IDETEN": self.IDETEN,
            "NOMTEN": self.NOMTEN,
            "INCTEN": self.INCTEN
        }


class TenResponseDTO:
    def __init__(self, ten):
        self.IDETEN = ten.IDETEN
        self.NOMTEN = ten.NOMTEN
        self.INCTEN = ten.INCTEN

    def to_dict(self):
        return self.__dict__