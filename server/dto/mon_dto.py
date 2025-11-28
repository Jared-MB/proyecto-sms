class monRequestDTO:
    def __init__(self, data):
        self.IDEMON = data.get("IDEMON")
        self.DESMON = data.get("DESMON")
        self.VALMON = data.get("VALMON")
        self.FECMON = data.get("FECMON")

    def to_dict(self):
        return {
            "IDEMON": self.IDEMON,
            "DESMON": self.DESMON,
            "VALMON": self.VALMON,
            "FECMON": self.FECMON
        }


class monResponseDTO:
    def __init__(self, mon):
        self.IDEMON = mon.IDEMON
        self.DESMON = mon.DESMON
        self.VALMON = mon.VALMON
        self.FECMON = mon.FECMON

    def to_dict(self):
        return self.__dict__
