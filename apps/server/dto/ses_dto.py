class sesRequestDTO:
    def __init__(self, data):
        self.IDESES = data.get("IDESES")
        self.PRISES = data.get("PRISES")
        self.PASSES = data.get("PASSES")

    def to_dict(self):
        return {
            "IDESES": self.IDESES,
            "PRISES": self.PRISES,
            "PASSES": self.PASSES
        }


class sesResponseDTO:
    def __init__(self, ses):
        self.IDESES = ses.IDESES
        self.PRISES = ses.PRISES
        self.PASSES = ses.PASSES

    def to_dict(self):
        return self.__dict__
