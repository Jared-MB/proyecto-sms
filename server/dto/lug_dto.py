class LugRequestDTO:
    def __init__(self, data):
        self.IDELUG = data.get("IDELUG")
        self.NOMLUG = data.get("NOMLUG")

    def to_dict(self):
        return {
            "IDELUG": self.IDELUG,
            "NOMLUG": self.NOMLUG
        }


class LugResponseDTO:
    def __init__(self, lug):
        self.IDELUG = lug.IDELUG
        self.NOMLUG = lug.NOMLUG

    def to_dict(self):
        return self.__dict__
