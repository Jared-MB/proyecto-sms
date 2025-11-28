from models import db
from models import TemJc
from services.util_service import convertirStringADate
from dto.temjc_dto import TemJcRequestDTO, TemJcResponseDTO

def crear_temjc(data):
    dto = TemJcRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = TemJc(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "TemJc creado correctamente"}

def leer_temjc(id):
    registro = TemJc.query.get(id)
    if not registro:
        return {"error": "TemJc no encontrado"}
    return TemJcResponseDTO(registro).to_dict()

def leer_todos_temjc():
    registros = TemJc.query.all()
    return [TemJcResponseDTO(r).to_dict() for r in registros]

def actualizar_temjc(id, data):
    registro = TemJc.query.get(id)
    if not registro:
        return {"error": "TemJc no encontrado"}
    
    dto = TemJcRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDETEM", "DESTEM", "JUNTEM", "IDETEM", "DESTEM", "JUNTEM"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "TemJc actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_temjc(id):
    registro = TemJc.query.get(id)
    if not registro:
        return {"error": "TemJc no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "TemJc eliminado correctamente"}
