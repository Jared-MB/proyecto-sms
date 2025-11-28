class EjmRequestDTO:
    def __init__(self, data):
        self.IDEEJM = data.get("IDEEJM")
        self.DESEJM = data.get("DESEJM")
        self.EJMTAC = data.get("EJMTAC")

    def to_dict(self):
        return {
            "IDEEJM": self.IDEEJM,
            "DESEJM": self.DESEJM,
            "EJMTAC": self.EJMTAC
        }


class EjmResponseDTO:
    def __init__(self, ejm):
        self.IDEEJM = ejm.IDEEJM
        self.DESEJM = ejm.DESEJM
        self.EJMTAC = ejm.EJMTAC

    def to_dict(self):
        return self.__dict__