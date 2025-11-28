from models import db
from models import Docmon
from services.util_service import convertirStringADate
from dto.docmon_dto import docmonRequestDTO, docmonResponseDTO

def crear_docmon(data):
    dto = docmonRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Docmon(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "docmon creado correctamente"}

def leer_docmon(id):
    registro = Docmon.query.get(id)
    if not registro:
        return {"error": "docmon no encontrado"}
    return docmonResponseDTO(registro).to_dict()

def leer_todos_docmon():
    registros = Docmon.query.all()
    return [docmonResponseDTO(r).to_dict() for r in registros]

def actualizar_docmon(id, data):
    registro = Docmon.query.get(id)
    if not registro:
        return {"error": "docmon no encontrado"}
    
    dto = docmonRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEDOCMON", "IDEDOC", "IDEMON", "IDEDOCMON", "IDEDOC", "IDEMON"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "docmon actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_docmon(id):
    registro = Docmon.query.get(id)
    if not registro:
        return {"error": "docmon no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "docmon eliminado correctamente"}
