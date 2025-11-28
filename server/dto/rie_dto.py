class rieRequestDTO:
    def __init__(self, data):
        self.IDERIE = data.get("IDERIE")
        self.DESRIE = data.get("DESRIE")
        self.CATRIE = data.get("CATRIE")

    def to_dict(self):
        return {
            "IDERIE": self.IDERIE,
            "DESRIE": self.DESRIE,
            "CATRIE": self.CATRIE
        }


class rieResponseDTO:
    def __init__(self, rie):
        self.IDERIE = rie.IDERIE
        self.DESRIE = rie.DESRIE
        self.CATRIE = rie.CATRIE

    def to_dict(self):
        return self.__dict__
