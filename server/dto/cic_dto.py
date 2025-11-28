class cicRequestDTO:
    def __init__(self, data):
        self.IDECIC = data.get("IDECIC")
        self.DESCIC = data.get("DESCIC")
        self.FECCIC = data.get("FECCIC")

    def to_dict(self):
        return {
            "IDECIC": self.IDECIC,
            "DESCIC": self.DESCIC,
            "FECCIC": self.FECCIC
        }


class cicResponseDTO:
    def __init__(self, cic):
        self.IDECIC = cic.IDECIC
        self.DESCIC = cic.DESCIC
        self.FECCIC = cic.FECCIC

    def to_dict(self):
        return self.__dict__
