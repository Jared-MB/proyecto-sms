from models import db
from models import Pel
from services.util_service import convertirStringADate
from dto.pel_dto import pelRequestDTO, pelResponseDTO

def crear_pel(data):
    dto = pelRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Pel(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "pel creado correctamente"}

def leer_pel(id):
    registro = Pel.query.get(id)
    if not registro:
        return {"error": "pel no encontrado"}
    return pelResponseDTO(registro).to_dict()

def leer_todos_pel():
    registros = Pel.query.all()
    return [pelResponseDTO(r).to_dict() for r in registros]

def actualizar_pel(id, data):
    registro = Pel.query.get(id)
    if not registro:
        return {"error": "pel no encontrado"}
    
    dto = pelRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEPEL", "DESPEL", "PELGRU", "IDEPEL", "DESPEL", "PELGRU"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "pel actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_pel(id):
    registro = Pel.query.get(id)
    if not registro:
        return {"error": "pel no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "pel eliminado correctamente"}
