from models import db
from models import Pro
from services.util_service import convertirStringADate
from dto.pro_dto import proRequestDTO, proResponseDTO

def crear_pro(data):
    dto = proRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Pro(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "pro creado correctamente"}

def leer_pro(id):
    registro = Pro.query.get(id)
    if not registro:
        return {"error": "pro no encontrado"}
    return proResponseDTO(registro).to_dict()

def leer_todos_pro():
    registros = Pro.query.all()
    return [proResponseDTO(r).to_dict() for r in registros]

def actualizar_pro(id, data):
    registro = Pro.query.get(id)
    if not registro:
        return {"error": "pro no encontrado"}
    
    dto = proRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEPRO", "DESPRO", "RESPRO", "FINPRO", "IDEPRO", "DESPRO", "RESPRO", "FINPRO"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "pro actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_pro(id):
    registro = Pro.query.get(id)
    if not registro:
        return {"error": "pro no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "pro eliminado correctamente"}
