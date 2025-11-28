class TecRequestDTO:
    def __init__(self, data):
        self.IDETEC = data.get("IDETEC")
        self.TIPTEC = data.get("TIPTEC")
        self.NOMTEC = data.get("NOMTEC")

    def to_dict(self):
        return {
            "IDETEC": self.IDETEC,
            "TIPTEC": self.TIPTEC,
            "NOMTEC": self.NOMTEC
        }


class TecResponseDTO:
    def __init__(self, tec):
        self.IDETEC = tec.IDETEC
        self.TIPTEC = tec.TIPTEC
        self.NOMTEC = tec.NOMTEC

    def to_dict(self):
        return self.__dict__