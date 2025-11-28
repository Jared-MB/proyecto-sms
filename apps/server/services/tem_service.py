from models import db
from models import Tem
from services.util_service import convertirStringADate
from dto.tem_dto import TemRequestDTO, TemResponseDTO

def crear_tem(data):
    dto = TemRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Tem(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Tem creado correctamente"}

def leer_tem(id):
    registro = Tem.query.get(id)
    if not registro:
        return {"error": "Tem no encontrado"}
    return TemResponseDTO(registro).to_dict()

def leer_todos_tem():
    registros = Tem.query.all()
    return [TemResponseDTO(r).to_dict() for r in registros]

def actualizar_tem(id, data):
    registro = Tem.query.get(id)
    if not registro:
        return {"error": "Tem no encontrado"}
    
    dto = TemRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDETEM", "TEMCAP", "DESTEM", "IDETEM", "TEMCAP", "DESTEM"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Tem actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_tem(id):
    registro = Tem.query.get(id)
    if not registro:
        return {"error": "Tem no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Tem eliminado correctamente"}
