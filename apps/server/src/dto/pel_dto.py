class pelRequestDTO:
    def __init__(self, data):
        self.IDEPEL = data.get("IDEPEL")
        self.DESPEL = data.get("DESPEL")
        self.PELGRU = data.get("PELGRU")

    def to_dict(self):
        return {
            "IDEPEL": self.IDEPEL,
            "DESPEL": self.DESPEL,
            "PELGRU": self.PELGRU
        }


class pelResponseDTO:
    def __init__(self, pel):
        self.IDEPEL = pel.IDEPEL
        self.DESPEL = pel.DESPEL
        self.PELGRU = pel.PELGRU

    def to_dict(self):
        return self.__dict__
