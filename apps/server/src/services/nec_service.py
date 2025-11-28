from models import db
from models import Nec
from services.util_service import convertirStringADate
from dto.nec_dto import NecRequestDTO, NecResponseDTO

def crear_nec(data):
    dto = NecRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Nec(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Nec creado correctamente"}

def leer_nec(id):
    registro = Nec.query.get(id)
    if not registro:
        return {"error": "Nec no encontrado"}
    return NecResponseDTO(registro).to_dict()

def leer_todos_nec():
    registros = Nec.query.all()
    return [NecResponseDTO(r).to_dict() for r in registros]

def actualizar_nec(id, data):
    registro = Nec.query.get(id)
    if not registro:
        return {"error": "Nec no encontrado"}
    
    dto = NecRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDENEC", "EDINEC", "DOCNEC", "NECCAP", "IDENEC", "EDINEC", "DOCNEC", "NECCAP"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Nec actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_nec(id):
    registro = Nec.query.get(id)
    if not registro:
        return {"error": "Nec no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Nec eliminado correctamente"}
