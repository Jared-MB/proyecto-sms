class CarRequestDTO:
    def __init__(self, data):
        self.IDECAR = data.get("IDECAR")
        self.NOMCAR = data.get("NOMCAR")
        self.COOCAR = data.get("COOCAR")
        self.CARCAR = data.get("CARCAR")
        self.ORGCAR = data.get("ORGCAR")

    def to_dict(self):
        return {
            "IDECAR": self.IDECAR,
            "NOMCAR": self.NOMCAR,
            "COOCAR": self.COOCAR,
            "CARCAR": self.CARCAR,
            "ORGCAR": self.ORGCAR
        }


class CarResponseDTO:
    def __init__(self, car):
        self.IDECAR = car.IDECAR
        self.NOMCAR = car.NOMCAR
        self.COOCAR = car.COOCAR
        self.CARCAR = car.CARCAR
        self.ORGCAR = car.ORGCAR

    def to_dict(self):
        return self.__dict__