class resRequestDTO:
    def __init__(self, data):
        self.IDERES = data.get("IDERES")
        self.DESRES = data.get("DESRES")
        self.FECRES = data.get("FECRES")

    def to_dict(self):
        return {
            "IDERES": self.IDERES,
            "DESRES": self.DESRES,
            "FECRES": self.FECRES
        }


class resResponseDTO:
    def __init__(self, res):
        self.IDERES = res.IDERES
        self.DESRES = res.DESRES
        self.FECRES = res.FECRES

    def to_dict(self):
        return self.__dict__
