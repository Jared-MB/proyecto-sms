class sugerenciasRequestDTO:
    def __init__(self, data):
        self.IDESUG = data.get("IDESUG")
        self.DESSUG = data.get("DESSUG")
        self.PERSUG = data.get("PERSUG")
        self.FECSUG = data.get("FECSUG")
        self.RESSUG = data.get("RESSUG")

    def to_dict(self):
        return {
            "IDESUG": self.IDESUG,
            "DESSUG": self.DESSUG,
            "PERSUG": self.PERSUG,
            "FECSUG": self.FECSUG,
            "RESSUG": self.RESSUG
        }


class sugerenciasResponseDTO:
    def __init__(self, sugerencias):
        self.IDESUG = sugerencias.IDESUG
        self.DESSUG = sugerencias.DESSUG
        self.PERSUG = sugerencias.PERSUG
        self.FECSUG = sugerencias.FECSUG
        self.RESSUG = sugerencias.RESSUG

    def to_dict(self):
        return self.__dict__
