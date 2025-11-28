from models import db
from models import Ejm
from services.util_service import convertirStringADate
from dto.ejm_dto import EjmRequestDTO, EjmResponseDTO

def crear_ejm(data):
    dto = EjmRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Ejm(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Ejm creado correctamente"}

def leer_ejm(id):
    registro = Ejm.query.get(id)
    if not registro:
        return {"error": "Ejm no encontrado"}
    return EjmResponseDTO(registro).to_dict()

def leer_todos_ejm():
    registros = Ejm.query.all()
    return [EjmResponseDTO(r).to_dict() for r in registros]

def actualizar_ejm(id, data):
    registro = Ejm.query.get(id)
    if not registro:
        return {"error": "Ejm no encontrado"}
    
    dto = EjmRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEEJM", "DESEJM", "EJMTAC", "IDEEJM", "DESEJM", "EJMTAC"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Ejm actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_ejm(id):
    registro = Ejm.query.get(id)
    if not registro:
        return {"error": "Ejm no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Ejm eliminado correctamente"}
