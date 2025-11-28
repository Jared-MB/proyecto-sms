class ExtRequestDTO:
    def __init__(self, data):
        self.IDEEXT = data.get("IDEEXT")
        self.APCEXT = data.get("APCEXT")
        self.AMCEXT = data.get("AMCEXT")
        self.NMCEXT = data.get("NMCEXT")
        self.TEMEXT = data.get("TEMEXT")
        self.EXTCAP = data.get("EXTCAP")
        self.EXTORG = data.get("EXTORG")

    def to_dict(self):
        return {
            "IDEEXT": self.IDEEXT,
            "APCEXT": self.APCEXT,
            "AMCEXT": self.AMCEXT,
            "NMCEXT": self.NMCEXT,
            "TEMEXT": self.TEMEXT,
            "EXTCAP": self.EXTCAP,
            "EXTORG": self.EXTORG
        }


class ExtResponseDTO:
    def __init__(self, ext):
        self.IDEEXT = ext.IDEEXT
        self.APCEXT = ext.APCEXT
        self.AMCEXT = ext.AMCEXT
        self.NMCEXT = ext.NMCEXT
        self.TEMEXT = ext.TEMEXT
        self.EXTCAP = ext.EXTCAP
        self.EXTORG = ext.EXTORG

    def to_dict(self):
        return self.__dict__