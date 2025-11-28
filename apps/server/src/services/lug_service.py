from models import db
from models import Lug
from services.util_service import convertirStringADate
from dto.lug_dto import LugRequestDTO, LugResponseDTO

def crear_lug(data):
    dto = LugRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Lug(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Lug creado correctamente"}

def leer_lug(id):
    registro = Lug.query.get(id)
    if not registro:
        return {"error": "Lug no encontrado"}
    return LugResponseDTO(registro).to_dict()

def leer_todos_lug():
    registros = Lug.query.all()
    return [LugResponseDTO(r).to_dict() for r in registros]

def actualizar_lug(id, data):
    registro = Lug.query.get(id)
    if not registro:
        return {"error": "Lug no encontrado"}
    
    dto = LugRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDELUG", "NOMLUG", "IDELUG", "NOMLUG"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Lug actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_lug(id):
    registro = Lug.query.get(id)
    if not registro:
        return {"error": "Lug no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Lug eliminado correctamente"}
