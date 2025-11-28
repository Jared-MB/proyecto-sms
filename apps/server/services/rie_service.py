from models import db
from models import Rie
from services.util_service import convertirStringADate
from dto.rie_dto import rieRequestDTO, rieResponseDTO

def crear_rie(data):
    dto = rieRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Rie(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "rie creado correctamente"}

def leer_rie(id):
    registro = Rie.query.get(id)
    if not registro:
        return {"error": "rie no encontrado"}
    return rieResponseDTO(registro).to_dict()

def leer_todos_rie():
    registros = Rie.query.all()
    return [rieResponseDTO(r).to_dict() for r in registros]

def actualizar_rie(id, data):
    registro = Rie.query.get(id)
    if not registro:
        return {"error": "rie no encontrado"}
    
    dto = rieRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDERIE", "DESRIE", "CATRIE", "IDERIE", "DESRIE", "CATRIE"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "rie actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_rie(id):
    registro = Rie.query.get(id)
    if not registro:
        return {"error": "rie no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "rie eliminado correctamente"}
