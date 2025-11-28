class docmonRequestDTO:
    def __init__(self, data):
        self.IDEDOCMON = data.get("IDEDOCMON")
        self.IDEDOC = data.get("IDEDOC")
        self.IDEMON = data.get("IDEMON")

    def to_dict(self):
        return {
            "IDEDOCMON": self.IDEDOCMON,
            "IDEDOC": self.IDEDOC,
            "IDEMON": self.IDEMON
        }


class docmonResponseDTO:
    def __init__(self, docmon):
        self.IDEDOCMON = docmon.IDEDOCMON
        self.IDEDOC = docmon.IDEDOC
        self.IDEMON = docmon.IDEMON

    def to_dict(self):
        return self.__dict__
