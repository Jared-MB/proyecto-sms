from models import db
from models import Bib
from services.util_service import convertirStringADate
from dto.bib_dto import BibRequestDTO, BibResponseDTO

def crear_bib(data):
    dto = BibRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Bib(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Bib creado correctamente"}

def leer_bib(id):
    registro = Bib.query.get(id)
    if not registro:
        return {"error": "Bib no encontrado"}
    return BibResponseDTO(registro).to_dict()

def leer_todos_bib():
    registros = Bib.query.all()
    return [BibResponseDTO(r).to_dict() for r in registros]

def actualizar_bib(id, data):
    registro = Bib.query.get(id)
    if not registro:
        return {"error": "Bib no encontrado"}
    
    dto = BibRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEBIB", "TDOCBIB", "NDOCBIB", "FDOCBIB", "EDOCBIB", "BIBCAP", "IDEBIB", "TDOCBIB", "NDOCBIB", "FDOCBIB", "EDOCBIB", "BIBCAP"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Bib actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_bib(id):
    registro = Bib.query.get(id)
    if not registro:
        return {"error": "Bib no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Bib eliminado correctamente"}
