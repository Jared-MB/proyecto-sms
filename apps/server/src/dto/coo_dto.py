class CooRequestDTO:
    def __init__(self, data):
        self.idecoo = data.get("idecoo")
        self.nomcoo = data.get("nomcoo")

    def to_dict(self):
        return {
            "idecoo": self.idecoo,
            "nomcoo": self.nomcoo
        }


class CooResponseDTO:
    def __init__(self, coo):
        self.idecoo = coo.IDECOO
        self.nomcoo = coo.NOMCOO

    def to_dict(self):
        return self.__dict__
