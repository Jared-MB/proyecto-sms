class visRequestDTO:
    def __init__(self, data):
        self.IDEVIS = data.get("IDEVIS")
        self.PUBVIS = data.get("PUBVIS")
        self.EMCVIS = data.get("EMCVIS")
        self.FECVIS = data.get("FECVIS")

    def to_dict(self):
        return {
            "IDEVIS": self.IDEVIS,
            "PUBVIS": self.PUBVIS,
            "EMCVIS": self.EMCVIS,
            "FECVIS": self.FECVIS
        }


class visResponseDTO:
    def __init__(self, vis):
        self.IDEVIS = vis.IDEVIS
        self.PUBVIS = vis.PUBVIS
        self.EMCVIS = vis.EMCVIS
        self.FECVIS = vis.FECVIS

    def to_dict(self):
        return self.__dict__
