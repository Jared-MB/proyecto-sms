from models import db
from models import Res
from services.util_service import convertirStringADate
from dto.res_dto import resRequestDTO, resResponseDTO

def crear_res(data):
    dto = resRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Res(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "res creado correctamente"}

def leer_res(id):
    registro = Res.query.get(id)
    if not registro:
        return {"error": "res no encontrado"}
    return resResponseDTO(registro).to_dict()

def leer_todos_res():
    registros = Res.query.all()
    return [resResponseDTO(r).to_dict() for r in registros]

def actualizar_res(id, data):
    registro = Res.query.get(id)
    if not registro:
        return {"error": "res no encontrado"}
    
    dto = resRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDERES", "DESRES", "FECRES", "IDERES", "DESRES", "FECRES"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "res actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_res(id):
    registro = Res.query.get(id)
    if not registro:
        return {"error": "res no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "res eliminado correctamente"}
