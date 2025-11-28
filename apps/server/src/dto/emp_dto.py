class EmpRequestDTO:
    def __init__(self, data):
        self.ideemp = data.get("ideemp")
        self.appemp = data.get("appemp")
        self.apmemp = data.get("apmemp")
        self.nomemp = data.get("nomemp")
        self.emaemp = data.get("emaemp")
        self.celemp = data.get("celemp")
        self.cel2emp = data.get("cel2emp")
        self.telofiemp = data.get("telofiemp")
        self.telofi2emp = data.get("telofi2emp")
        self.extemp = data.get("extemp")
        self.fotemp = data.get("fotemp")

    def to_dict(self):
        return {
            "ideemp": self.ideemp,
            "appemp": self.appemp,
            "apmemp": self.apmemp,
            "nomemp": self.nomemp,
            "emaemp": self.emaemp,
            "celemp": self.celemp,
            "cel2emp": self.cel2emp,
            "telofiemp": self.telofiemp,
            "telofi2emp": self.telofi2emp,
            "extemp": self.extemp,
            "fotemp": self.fotemp
        }


class EmpResponseDTO:
    def __init__(self, emp):
        self.ideemp = emp.IDEEMP
        self.appemp = emp.APPEMP
        self.apmemp = emp.APMEMP
        self.nomemp = emp.NOMEMP
        self.emaemp = emp.EMAEMP
        self.celemp = emp.CELEMP
        self.cel2emp = emp.CEL2EMP
        self.telofiemp = emp.TELOFIEMP
        self.telofi2emp = emp.TELOFI2EMP
        self.extemp = emp.EXTEMP
        self.fotemp = emp.FOTEMP

    def to_dict(self):
        return self.__dict__
