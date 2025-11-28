class TopRequestDTO:
    def __init__(self, data):
        self.IDETOP = data.get("IDETOP")
        self.NMTTOP = data.get("NMTTOP")
        self.DESTOP = data.get("DESTOP")

    def to_dict(self):
        return {
            "IDETOP": self.IDETOP,
            "NMTTOP": self.NMTTOP,
            "DESTOP": self.DESTOP
        }


class TopResponseDTO:
    def __init__(self, top):
        self.IDETOP = top.IDETOP
        self.NMTTOP = top.NMTTOP
        self.DESTOP = top.DESTOP

    def to_dict(self):
        return self.__dict__