class TpoRequestDTO:
    def __init__(self, data):
        self.IDETPO = data.get("IDETPO")
        self.NOMTPO = data.get("NOMTPO")
        self.TCATPO = data.get("TCATPO")

    def to_dict(self):
        return {
            "IDETPO": self.IDETPO,
            "NOMTPO": self.NOMTPO,
            "TCATPO": self.TCATPO
        }


class TpoResponseDTO:
    def __init__(self, tpo):
        self.IDETPO = tpo.IDETPO
        self.NOMTPO = tpo.NOMTPO
        self.TCATPO = tpo.TCATPO

    def to_dict(self):
        return self.__dict__