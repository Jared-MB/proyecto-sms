class comRequestDTO:
    def __init__(self, data):
        self.IDECOM = data.get("IDECOM")
        self.DESCOM = data.get("DESCOM")
        self.FECCOM = data.get("FECCOM")

    def to_dict(self):
        return {
            "IDECOM": self.IDECOM,
            "DESCOM": self.DESCOM,
            "FECCOM": self.FECCOM
        }


class comResponseDTO:
    def __init__(self, com):
        self.IDECOM = com.IDECOM
        self.DESCOM = com.DESCOM
        self.FECCOM = com.FECCOM

    def to_dict(self):
        return self.__dict__
