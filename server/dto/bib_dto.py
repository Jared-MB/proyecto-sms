class BibRequestDTO:
    def __init__(self, data):
        self.IDEBIB = data.get("IDEBIB")
        self.TDOCBIB = data.get("TDOCBIB")
        self.NDOCBIB = data.get("NDOCBIB")
        self.FDOCBIB = data.get("FDOCBIB")
        self.EDOCBIB = data.get("EDOCBIB")
        self.BIBCAP = data.get("BIBCAP")

    def to_dict(self):
        return {
            "IDEBIB": self.IDEBIB,
            "TDOCBIB": self.TDOCBIB,
            "NDOCBIB": self.NDOCBIB,
            "FDOCBIB": self.FDOCBIB,
            "EDOCBIB": self.EDOCBIB,
            "BIBCAP": self.BIBCAP
        }


class BibResponseDTO:
    def __init__(self, bib):
        self.IDEBIB = bib.IDEBIB
        self.TDOCBIB = bib.TDOCBIB
        self.NDOCBIB = bib.NDOCBIB
        self.FDOCBIB = bib.FDOCBIB
        self.EDOCBIB = bib.EDOCBIB
        self.BIBCAP = bib.BIBCAP

    def to_dict(self):
        return self.__dict__