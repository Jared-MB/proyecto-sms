from models import db
from models import Evi
from services.util_service import convertirStringADate
from dto.evi_dto import eviRequestDTO, eviResponseDTO

def crear_evi(data):
    dto = eviRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Evi(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "evi creado correctamente"}

def leer_evi(id):
    registro = Evi.query.get(id)
    if not registro:
        return {"error": "evi no encontrado"}
    return eviResponseDTO(registro).to_dict()

def leer_todos_evi():
    registros = Evi.query.all()
    return [eviResponseDTO(r).to_dict() for r in registros]

def actualizar_evi(id, data):
    registro = Evi.query.get(id)
    if not registro:
        return {"error": "evi no encontrado"}
    
    dto = eviRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEEVI", "DESCEVI", "TIPEVI", "FECEVI", "IDEEVI", "DESCEVI", "TIPEVI", "FECEVI"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "evi actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_evi(id):
    registro = Evi.query.get(id)
    if not registro:
        return {"error": "evi no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "evi eliminado correctamente"}
