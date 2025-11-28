class PerRequestDTO:
    def __init__(self, data):
        self.IDEPER = data.get("IDEPER")
        self.EMPPER = data.get("EMPPER")
        self.CARPER = data.get("CARPER")
        self.FECFIN = data.get("FECFIN")

    def to_dict(self):
        return {
            "IDEPER": self.IDEPER,
            "EMPPER": self.EMPPER,
            "CARPER": self.CARPER,
            "FECFIN": self.FECFIN
        }


class PerResponseDTO:
    def __init__(self, per):
        self.IDEPER = per.IDEPER
        self.EMPPER = per.EMPPER
        self.CARPER = per.CARPER
        self.FECFIN = per.FECFIN

    def to_dict(self):
        return self.__dict__