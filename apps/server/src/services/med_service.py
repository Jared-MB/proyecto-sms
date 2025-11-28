from models import db
from models import Med
from services.util_service import convertirStringADate
from dto.med_dto import MedRequestDTO, MedResponseDTO

def crear_med(data):
    dto = MedRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Med(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Med creado correctamente"}

def leer_med(id):
    registro = Med.query.get(id)
    if not registro:
        return {"error": "Med no encontrado"}
    return MedResponseDTO(registro).to_dict()

def leer_todos_med():
    registros = Med.query.all()
    return [MedResponseDTO(r).to_dict() for r in registros]

def actualizar_med(id, data):
    registro = Med.query.get(id)
    if not registro:
        return {"error": "Med no encontrado"}
    
    dto = MedRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEMED", "NOMMED", "IMGMED", "IDEMED", "NOMMED", "IMGMED"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Med actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_med(id):
    registro = Med.query.get(id)
    if not registro:
        return {"error": "Med no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Med eliminado correctamente"}
