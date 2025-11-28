class eviRequestDTO:
    def __init__(self, data):
        self.IDEEVI = data.get("IDEEVI")
        self.DESCEVI = data.get("DESCEVI")
        self.TIPEVI = data.get("TIPEVI")
        self.FECEVI = data.get("FECEVI")

    def to_dict(self):
        return {
            "IDEEVI": self.IDEEVI,
            "DESCEVI": self.DESCEVI,
            "TIPEVI": self.TIPEVI,
            "FECEVI": self.FECEVI
        }


class eviResponseDTO:
    def __init__(self, evi):
        self.IDEEVI = evi.IDEEVI
        self.DESCEVI = evi.DESCEVI
        self.TIPEVI = evi.TIPEVI
        self.FECEVI = evi.FECEVI

    def to_dict(self):
        return self.__dict__
