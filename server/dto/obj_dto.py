class ObjRequestDTO:
    def __init__(self, data):
        self.IDEOBJ = data.get("IDEOBJ")
        self.TIPOBJ = data.get("TIPOBJ")
        self.OBJCAP = data.get("OBJCAP")
        self.DESOBJ = data.get("DESOBJ")

    def to_dict(self):
        return {
            "IDEOBJ": self.IDEOBJ,
            "TIPOBJ": self.TIPOBJ,
            "OBJCAP": self.OBJCAP,
            "DESOBJ": self.DESOBJ
        }


class ObjResponseDTO:
    def __init__(self, obj):
        self.IDEOBJ = obj.IDEOBJ
        self.TIPOBJ = obj.TIPOBJ
        self.OBJCAP = obj.OBJCAP
        self.DESOBJ = obj.DESOBJ

    def to_dict(self):
        return self.__dict__