class TemJcRequestDTO:
    def __init__(self, data):
        self.IDETEM = data.get("IDETEM")
        self.DESTEM = data.get("DESTEM")
        self.JUNTEM = data.get("JUNTEM")

    def to_dict(self):
        return {
            "IDETEM": self.IDETEM,
            "DESTEM": self.DESTEM,
            "JUNTEM": self.JUNTEM
        }


class TemJcResponseDTO:
    def __init__(self, temjc):
        self.IDETEM = temjc.IDETEM
        self.DESTEM = temjc.DESTEM
        self.JUNTEM = temjc.JUNTEM

    def to_dict(self):
        return self.__dict__
