class cauRequestDTO:
    def __init__(self, data):
        self.IDECAU = data.get("IDECAU")
        self.DESCAU = data.get("DESCAU")
        self.TIPCAU = data.get("TIPCAU")

    def to_dict(self):
        return {
            "IDECAU": self.IDECAU,
            "DESCAU": self.DESCAU,
            "TIPCAU": self.TIPCAU
        }


class cauResponseDTO:
    def __init__(self, cau):
        self.IDECAU = cau.IDECAU
        self.DESCAU = cau.DESCAU
        self.TIPCAU = cau.TIPCAU

    def to_dict(self):
        return self.__dict__
