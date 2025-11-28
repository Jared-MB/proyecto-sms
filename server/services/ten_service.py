from models import db
from models import Ten
from services.util_service import convertirStringADate
from dto.ten_dto import TenRequestDTO, TenResponseDTO

def crear_ten(data):
    dto = TenRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Ten(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Ten creado correctamente"}

def leer_ten(id):
    registro = Ten.query.get(id)
    if not registro:
        return {"error": "Ten no encontrado"}
    return TenResponseDTO(registro).to_dict()

def leer_todos_ten():
    registros = Ten.query.all()
    return [TenResponseDTO(r).to_dict() for r in registros]

def actualizar_ten(id, data):
    registro = Ten.query.get(id)
    if not registro:
        return {"error": "Ten no encontrado"}
    
    dto = TenRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDETEN", "NOMTEN", "INCTEN", "IDETEN", "NOMTEN", "INCTEN"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Ten actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_ten(id):
    registro = Ten.query.get(id)
    if not registro:
        return {"error": "Ten no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Ten eliminado correctamente"}
