from models import db
from models import Sugerencias
from services.util_service import convertirStringADate
from dto.sugerencias_dto import sugerenciasRequestDTO, sugerenciasResponseDTO

def crear_sugerencias(data):
    dto = sugerenciasRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Sugerencias(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "sugerencias creado correctamente"}

def leer_sugerencias(id):
    registro = Sugerencias.query.get(id)
    if not registro:
        return {"error": "sugerencias no encontrado"}
    return sugerenciasResponseDTO(registro).to_dict()

def leer_todos_sugerencias():
    registros = Sugerencias.query.all()
    return [sugerenciasResponseDTO(r).to_dict() for r in registros]

def actualizar_sugerencias(id, data):
    registro = Sugerencias.query.get(id)
    if not registro:
        return {"error": "sugerencias no encontrado"}
    
    dto = sugerenciasRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDESUG", "DESSUG", "PERSUG", "FECSUG", "RESSUG", "IDESUG", "DESSUG", "PERSUG", "FECSUG", "RESSUG"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "sugerencias actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_sugerencias(id):
    registro = Sugerencias.query.get(id)
    if not registro:
        return {"error": "sugerencias no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "sugerencias eliminado correctamente"}
