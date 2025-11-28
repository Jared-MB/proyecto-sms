class ConRequestDTO:
    def __init__(self, data):
        self.idecon = data.get("idecon")
        self.nomcon = data.get("nomcon")
        self.descon = data.get("descon")
        self.tipcon = data.get("tipcon")

    def to_dict(self):
        return {
            "idecon": self.idecon,
            "nomcon": self.nomcon,
            "descon": self.descon,
            "tipcon": self.tipcon
        }


class ConResponseDTO:
    def __init__(self, con):
        self.idecon = con.idecon
        self.nomcon = con.nomcon
        self.descon = con.descon
        self.tipcon = con.tipcon

    def to_dict(self):
        return self.__dict__
