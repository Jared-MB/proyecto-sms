class DiaRequestDTO:
    def __init__(self, data):
        self.idedia = data.get("idedia")
        self.fecdia = data.get("fecdia")
        self.fecfin = data.get("fecfin")
        self.fecini = data.get("fecini")
        self.per_dia = data.get("per_dia")

    def to_dict(self):
        return {
            "idedia": self.idedia,
            "fecdia": self.fecdia,
            "fecfin": self.fecfin,
            "fecini": self.fecini,
            "per_dia": self.per_dia
        }


class DiaResponseDTO:
    def __init__(self, dia):
        self.idedia = dia.IDEDIA
        self.fecdia = dia.FECDIA
        self.fecfin = dia.FECFIN
        self.fecini = dia.FECINI
        self.per_dia = dia.PER_DIA

    def to_dict(self):
        return self.__dict__
