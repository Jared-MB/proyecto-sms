from models import db
from models import Cap
from services.util_service import convertirStringADate
from dto.cap_dto import CapRequestDTO, CapResponseDTO

def crear_cap(data):
    dto = CapRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Cap(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Cap creado correctamente"}

def leer_cap(id):
    registro = Cap.query.get(id)
    if not registro:
        return {"error": "Cap no encontrado"}
    return CapResponseDTO(registro).to_dict()

def leer_todos_cap():
    registros = Cap.query.all()
    return [CapResponseDTO(r).to_dict() for r in registros]

def actualizar_cap(id, data):
    registro = Cap.query.get(id)
    if not registro:
        return {"error": "Cap no encontrado"}
    
    dto = CapRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["idecap", "pobcap", "ncucap", "hrtcap", "htecap", "hprcap", "fincap", "ffncap", "hincap", "hfncap", "lugcap", "reldia", "diacap", "verifc", "idecap", "pobcap", "ncucap", "hrtcap", "htecap", "hprcap", "fincap", "ffncap", "hincap", "hfncap", "lugcap", "reldia", "diacap", "verifc"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Cap actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_cap(id):
    registro = Cap.query.get(id)
    if not registro:
        return {"error": "Cap no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Cap eliminado correctamente"}
