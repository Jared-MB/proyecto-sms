class TemRequestDTO:
    def __init__(self, data):
        self.IDETEM = data.get("IDETEM")
        self.TEMCAP = data.get("TEMCAP")
        self.DESTEM = data.get("DESTEM")

    def to_dict(self):
        return {
            "IDETEM": self.IDETEM,
            "TEMCAP": self.TEMCAP,
            "DESTEM": self.DESTEM
        }


class TemResponseDTO:
    def __init__(self, tem):
        self.IDETEM = tem.IDETEM
        self.TEMCAP = tem.TEMCAP
        self.DESTEM = tem.DESTEM

    def to_dict(self):
        return self.__dict__