class monproRequestDTO:
    def __init__(self, data):
        self.IDEMONPRO = data.get("IDEMONPRO")
        self.IDEMON = data.get("IDEMON")
        self.IDEPRO = data.get("IDEPRO")

    def to_dict(self):
        return {
            "IDEMONPRO": self.IDEMONPRO,
            "IDEMON": self.IDEMON,
            "IDEPRO": self.IDEPRO
        }


class monproResponseDTO:
    def __init__(self, monpro):
        self.IDEMONPRO = monpro.IDEMONPRO
        self.IDEMON = monpro.IDEMON
        self.IDEPRO = monpro.IDEPRO

    def to_dict(self):
        return self.__dict__
