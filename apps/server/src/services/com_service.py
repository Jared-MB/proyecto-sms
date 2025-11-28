from models import db
from models import Com
from services.util_service import convertirStringADate
from dto.com_dto import comRequestDTO, comResponseDTO

def crear_com(data):
    dto = comRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Com(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "com creado correctamente"}

def leer_com(id):
    registro = Com.query.get(id)
    if not registro:
        return {"error": "com no encontrado"}
    return comResponseDTO(registro).to_dict()

def leer_todos_com():
    registros = Com.query.all()
    return [comResponseDTO(r).to_dict() for r in registros]

def actualizar_com(id, data):
    registro = Com.query.get(id)
    if not registro:
        return {"error": "com no encontrado"}
    
    dto = comRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDECOM", "DESCOM", "FECCOM", "IDECOM", "DESCOM", "FECCOM"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "com actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_com(id):
    registro = Com.query.get(id)
    if not registro:
        return {"error": "com no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "com eliminado correctamente"}
