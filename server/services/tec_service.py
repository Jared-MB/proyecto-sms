from models import db
from models import Tec
from services.util_service import convertirStringADate
from dto.tec_dto import TecRequestDTO, TecResponseDTO

def crear_tec(data):
    dto = TecRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Tec(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Tec creado correctamente"}

def leer_tec(id):
    registro = Tec.query.get(id)
    if not registro:
        return {"error": "Tec no encontrado"}
    return TecResponseDTO(registro).to_dict()

def leer_todos_tec():
    registros = Tec.query.all()
    return [TecResponseDTO(r).to_dict() for r in registros]

def actualizar_tec(id, data):
    registro = Tec.query.get(id)
    if not registro:
        return {"error": "Tec no encontrado"}
    
    dto = TecRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDETEC", "TIPTEC", "NOMTEC", "IDETEC", "TIPTEC", "NOMTEC"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Tec actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_tec(id):
    registro = Tec.query.get(id)
    if not registro:
        return {"error": "Tec no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Tec eliminado correctamente"}
