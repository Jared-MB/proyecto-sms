class CapRequestDTO:
    def __init__(self, data):
        self.idecap = data.get("idecap")
        self.pobcap = data.get("pobcap")
        self.ncucap = data.get("ncucap")
        self.hrtcap = data.get("hrtcap")
        self.htecap = data.get("htecap")
        self.hprcap = data.get("hprcap")
        self.fincap = data.get("fincap")
        self.ffncap = data.get("ffncap")
        self.hincap = data.get("hincap")
        self.hfncap = data.get("hfncap")
        self.lugcap = data.get("lugcap")
        self.reldia = data.get("reldia")
        self.diacap = data.get("diacap")
        self.verifc = data.get("verifc")

    def to_dict(self):
        return {
            "idecap": self.idecap,
            "pobcap": self.pobcap,
            "ncucap": self.ncucap,
            "hrtcap": self.hrtcap,
            "htecap": self.htecap,
            "hprcap": self.hprcap,
            "fincap": self.fincap,
            "ffncap": self.ffncap,
            "hincap": self.hincap,
            "hfncap": self.hfncap,
            "lugcap": self.lugcap,
            "reldia": self.reldia,
            "diacap": self.diacap,
            "verifc": self.verifc
        }


class CapResponseDTO:
    def __init__(self, cap):
        self.idecap = cap.IDECAP
        self.pobcap = cap.POBCAP
        self.ncucap = cap.NCUCAP
        self.hrtcap = cap.HRTCAP
        self.htecap = cap.HTECAP
        self.hprcap = cap.HPRCAP
        self.fincap = cap.FINCAP
        self.ffncap = cap.FFNCAP
        self.hincap = cap.HINCAP
        self.hfncap = cap.HFNCAP
        self.lugcap = cap.LUGCAP
        self.reldia = cap.RELDIA
        self.diacap = cap.DIACAP
        self.verifc = cap.VERIFC

    def to_dict(self):
        return self.__dict__
