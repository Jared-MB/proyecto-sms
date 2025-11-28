from models import db
from models import ProJc
from services.util_service import convertirStringADate
from dto.projc_dto import projcRequestDTO, projcResponseDTO

def crear_projc(data):
    dto = projcRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = ProJc(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "projc creado correctamente"}

def leer_projc(id):
    registro = ProJc.query.get(id)
    if not registro:
        return {"error": "projc no encontrado"}
    return projcResponseDTO(registro).to_dict()

def leer_todos_projc():
    registros = ProJc.query.all()
    return [projcResponseDTO(r).to_dict() for r in registros]

def actualizar_projc(id, data):
    registro = ProJc.query.get(id)
    if not registro:
        return {"error": "projc no encontrado"}
    
    dto = projcRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEPRO", "DESPRO", "TIEPRO", "ESTPRO", "RESPRO", "TEMPRO", "IDEPRO", "DESPRO", "TIEPRO", "ESTPRO", "RESPRO", "TEMPRO"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "projc actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_projc(id):
    registro = ProJc.query.get(id)
    if not registro:
        return {"error": "projc no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "projc eliminado correctamente"}
