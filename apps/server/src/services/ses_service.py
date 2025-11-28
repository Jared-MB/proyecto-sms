from models import db
from models import Ses
from services.util_service import convertirStringADate
from dto.ses_dto import sesRequestDTO, sesResponseDTO

def crear_ses(data):
    dto = sesRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Ses(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "ses creado correctamente"}

def leer_ses(id):
    registro = Ses.query.get(id)
    if not registro:
        return {"error": "ses no encontrado"}
    return sesResponseDTO(registro).to_dict()

def leer_todos_ses():
    registros = Ses.query.all()
    return [sesResponseDTO(r).to_dict() for r in registros]

def actualizar_ses(id, data):
    registro = Ses.query.get(id)
    if not registro:
        return {"error": "ses no encontrado"}
    
    dto = sesRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDESES", "PRISES", "PASSES", "IDESES", "PRISES", "PASSES"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "ses actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_ses(id):
    registro = Ses.query.get(id)
    if not registro:
        return {"error": "ses no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "ses eliminado correctamente"}
