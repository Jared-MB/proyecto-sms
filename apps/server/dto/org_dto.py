class OrgRequestDTO:
    def __init__(self, data):
        self.IDEORG = data.get("IDEORG")
        self.NOMORG = data.get("NOMORG")
        self.DIRORG = data.get("DIRORG")
        self.TELORG = data.get("TELORG")

    def to_dict(self):
        return {
            "IDEORG": self.IDEORG,
            "NOMORG": self.NOMORG,
            "DIRORG": self.DIRORG,
            "TELORG": self.TELORG
        }


class OrgResponseDTO:
    def __init__(self, org):
        self.IDEORG = org.IDEORG
        self.NOMORG = org.NOMORG
        self.DIRORG = org.DIRORG
        self.TELORG = org.TELORG

    def to_dict(self):
        return self.__dict__