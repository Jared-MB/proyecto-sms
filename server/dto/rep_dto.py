class repRequestDTO:
    def __init__(self, data):
        self.IDEREP = data.get("IDEREP")
        self.CONREP = data.get("CONREP")
        self.FECEVE = data.get("FECEVE")
        self.FECREP = data.get("FECREP")
        self.FREREP = data.get("FREREP")
        self.LUGREP = data.get("LUGREP")
        self.CANREP = data.get("CANREP")
        self.PERREP = data.get("PERREP")
        self.OBSREP = data.get("OBSREP")

    def to_dict(self):
        return {
            "IDEREP": self.IDEREP,
            "CONREP": self.CONREP,
            "FECEVE": self.FECEVE,
            "FECREP": self.FECREP,
            "FREREP": self.FREREP,
            "LUGREP": self.LUGREP,
            "CANREP": self.CANREP,
            "PERREP": self.PERREP,
            "OBSREP": self.OBSREP
        }


class repResponseDTO:
    def __init__(self, rep):
        self.IDEREP = rep.IDEREP
        self.CONREP = rep.CONREP
        self.FECEVE = rep.FECEVE
        self.FECREP = rep.FECREP
        self.FREREP = rep.FREREP
        self.LUGREP = rep.LUGREP
        self.CANREP = rep.CANREP
        self.PERREP = rep.PERREP
        self.OBSREP = rep.OBSREP

    def to_dict(self):
        return self.__dict__
