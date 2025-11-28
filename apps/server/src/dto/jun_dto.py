class JunRequestDTO:
    def __init__(self, data):
        self.idejun = data.get("idejun")
        self.fecjun = data.get("fecjun")
        self.lugjun = data.get("lugjun")
        self.fefjun = data.get("fefjun")
        self.minjun = data.get("minjun")
        self.diajun = data.get("diajun")

    def to_dict(self):
        return {
            "idejun": self.idejun,
            "fecjun": self.fecjun,
            "lugjun": self.lugjun,
            "fefjun": self.fefjun,
            "minjun": self.minjun,
            "diajun": self.diajun
        }


class JunResponseDTO:
    def __init__(self, jun):
        self.idejun = jun.IDEJUN
        self.fecjun = jun.FECJUN
        self.lugjun = jun.LUGJUN
        self.fefjun = jun.FEFJUN
        self.minjun = jun.MINJUN
        self.diajun = jun.DIAJUN

    def to_dict(self):
        return self.__dict__
