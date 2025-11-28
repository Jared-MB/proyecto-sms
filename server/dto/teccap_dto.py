class TeccapRequestDTO:
    def __init__(self, data):
        self.IDETECCAP = data.get("IDETECCAP")
        self.TECCAPCAP = data.get("TECCAPCAP")
        self.TECCAPTEC = data.get("TECCAPTEC")

    def to_dict(self):
        return {
            "IDETECCAP": self.IDETECCAP,
            "TECCAPCAP": self.TECCAPCAP,
            "TECCAPTEC": self.TECCAPTEC
        }


class TeccapResponseDTO:
    def __init__(self, teccap):
        self.IDETECCAP = teccap.IDETECCAP
        self.TECCAPCAP = teccap.TECCAPCAP
        self.TECCAPTEC = teccap.TECCAPTEC

    def to_dict(self):
        return self.__dict__