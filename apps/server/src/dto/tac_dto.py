class TacRequestDTO:
    def __init__(self, data):
        self.IDETAC = data.get("IDETAC")
        self.DESTAC = data.get("DESTAC")
        self.TACTOP = data.get("TACTOP")

    def to_dict(self):
        return {
            "IDETAC": self.IDETAC,
            "DESTAC": self.DESTAC,
            "TACTOP": self.TACTOP
        }


class TacResponseDTO:
    def __init__(self, tac):
        self.IDETAC = tac.IDETAC
        self.DESTAC = tac.DESTAC
        self.TACTOP = tac.TACTOP

    def to_dict(self):
        return self.__dict__
