from models import db
from models import Dia
from services.util_service import convertirStringADate
from dto.dia_dto import DiaRequestDTO, DiaResponseDTO

def crear_dia(data):
    dto = DiaRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Dia(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Dia creado correctamente"}

def leer_dia(id):
    registro = Dia.query.get(id)
    if not registro:
        return {"error": "Dia no encontrado"}
    return DiaResponseDTO(registro).to_dict()

def leer_todos_dia():
    registros = Dia.query.all()
    return [DiaResponseDTO(r).to_dict() for r in registros]

def actualizar_dia(id, data):
    registro = Dia.query.get(id)
    if not registro:
        return {"error": "Dia no encontrado"}
    
    dto = DiaRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["idedia", "fecdia", "fecfin", "fecini", "per_dia", "idedia", "fecdia", "fecfin", "fecini", "per_dia"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Dia actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_dia(id):
    registro = Dia.query.get(id)
    if not registro:
        return {"error": "Dia no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Dia eliminado correctamente"}
