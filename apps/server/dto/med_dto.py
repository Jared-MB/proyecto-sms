class MedRequestDTO:
    def __init__(self, data):
        self.IDEMED = data.get("IDEMED")
        self.NOMMED = data.get("NOMMED")
        self.IMGMED = data.get("IMGMED")

    def to_dict(self):
        return {
            "IDEMED": self.IDEMED,
            "NOMMED": self.NOMMED,
            "IMGMED": self.IMGMED
        }


class MedResponseDTO:
    def __init__(self, med):
        self.IDEMED = med.IDEMED
        self.NOMMED = med.NOMMED
        self.IMGMED = med.IMGMED

    def to_dict(self):
        return self.__dict__
