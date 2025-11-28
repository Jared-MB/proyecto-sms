class docRequestDTO:
    def __init__(self, data):
        self.IDEDOC = data.get("IDEDOC")
        self.DESDOC = data.get("DESDOC")
        self.TIPDOC = data.get("TIPDOC")
        self.FECDOC = data.get("FECDOC")

    def to_dict(self):
        return {
            "IDEDOC": self.IDEDOC,
            "DESDOC": self.DESDOC,
            "TIPDOC": self.TIPDOC,
            "FECDOC": self.FECDOC
        }


class docResponseDTO:
    def __init__(self, doc):
        self.IDEDOC = doc.IDEDOC
        self.DESDOC = doc.DESDOC
        self.TIPDOC = doc.TIPDOC
        self.FECDOC = doc.FECDOC

    def to_dict(self):
        return self.__dict__
