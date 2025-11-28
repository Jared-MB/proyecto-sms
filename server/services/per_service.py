from models import db
from models import Per
from services.util_service import convertirStringADate
from dto.per_dto import PerRequestDTO, PerResponseDTO

def crear_per(data):
    dto = PerRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Per(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Per creado correctamente"}

def leer_per(id):
    registro = Per.query.get(id)
    if not registro:
        return {"error": "Per no encontrado"}
    return PerResponseDTO(registro).to_dict()

def leer_todos_per():
    registros = Per.query.all()
    return [PerResponseDTO(r).to_dict() for r in registros]

def actualizar_per(id, data):
    registro = Per.query.get(id)
    if not registro:
        return {"error": "Per no encontrado"}
    
    dto = PerRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEPER", "EMPPER", "CARPER", "FECFIN", "IDEPER", "EMPPER", "CARPER", "FECFIN"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Per actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_per(id):
    registro = Per.query.get(id)
    if not registro:
        return {"error": "Per no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Per eliminado correctamente"}
