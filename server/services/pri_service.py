from models import db
from models import Pri
from services.util_service import convertirStringADate
from dto.pri_dto import PriRequestDTO, PriResponseDTO

def crear_pri(data):
    dto = PriRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Pri(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Pri creado correctamente"}

def leer_pri(id):
    registro = Pri.query.get(id)
    if not registro:
        return {"error": "Pri no encontrado"}
    return PriResponseDTO(registro).to_dict()

def leer_todos_pri():
    registros = Pri.query.all()
    return [PriResponseDTO(r).to_dict() for r in registros]

def actualizar_pri(id, data):
    registro = Pri.query.get(id)
    if not registro:
        return {"error": "Pri no encontrado"}
    
    dto = PriRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEPRI", "NOMPRI", "IDEPRI", "NOMPRI"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Pri actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_pri(id):
    registro = Pri.query.get(id)
    if not registro:
        return {"error": "Pri no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Pri eliminado correctamente"}
