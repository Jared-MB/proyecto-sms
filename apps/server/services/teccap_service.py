from models import db
from models import Teccap
from services.util_service import convertirStringADate
from dto.teccap_dto import TeccapRequestDTO, TeccapResponseDTO

def crear_teccap(data):
    dto = TeccapRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Teccap(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Teccap creado correctamente"}

def leer_teccap(id):
    registro = Teccap.query.get(id)
    if not registro:
        return {"error": "Teccap no encontrado"}
    return TeccapResponseDTO(registro).to_dict()

def leer_todos_teccap():
    registros = Teccap.query.all()
    return [TeccapResponseDTO(r).to_dict() for r in registros]

def actualizar_teccap(id, data):
    registro = Teccap.query.get(id)
    if not registro:
        return {"error": "Teccap no encontrado"}
    
    dto = TeccapRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDETECCAP", "TECCAPCAP", "TECCAPTEC", "IDETECCAP", "TECCAPCAP", "TECCAPTEC"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Teccap actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_teccap(id):
    registro = Teccap.query.get(id)
    if not registro:
        return {"error": "Teccap no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Teccap eliminado correctamente"}
