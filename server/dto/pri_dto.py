class PriRequestDTO:
    def __init__(self, data):
        self.IDEPRI = data.get("IDEPRI")
        self.NOMPRI = data.get("NOMPRI")

    def to_dict(self):
        return {
            "IDEPRI": self.IDEPRI,
            "NOMPRI": self.NOMPRI
        }


class PriResponseDTO:
    def __init__(self, pri):
        self.IDEPRI = pri.IDEPRI
        self.NOMPRI = pri.NOMPRI

    def to_dict(self):
        return self.__dict__