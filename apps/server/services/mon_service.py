from models import db
from models import Mon
from services.util_service import convertirStringADate
from dto.mon_dto import monRequestDTO, monResponseDTO

def crear_mon(data):
    dto = monRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Mon(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "mon creado correctamente"}

def leer_mon(id):
    registro = Mon.query.get(id)
    if not registro:
        return {"error": "mon no encontrado"}
    return monResponseDTO(registro).to_dict()

def leer_todos_mon():
    registros = Mon.query.all()
    return [monResponseDTO(r).to_dict() for r in registros]

def actualizar_mon(id, data):
    registro = Mon.query.get(id)
    if not registro:
        return {"error": "mon no encontrado"}
    
    dto = monRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEMON", "DESMON", "VALMON", "FECMON", "IDEMON", "DESMON", "VALMON", "FECMON"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "mon actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_mon(id):
    registro = Mon.query.get(id)
    if not registro:
        return {"error": "mon no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "mon eliminado correctamente"}
