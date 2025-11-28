from models import db
from models import Doc
from services.util_service import convertirStringADate
from dto.doc_dto import docRequestDTO, docResponseDTO

def crear_doc(data):
    dto = docRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Doc(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "doc creado correctamente"}

def leer_doc(id):
    registro = Doc.query.get(id)
    if not registro:
        return {"error": "doc no encontrado"}
    return docResponseDTO(registro).to_dict()

def leer_todos_doc():
    registros = Doc.query.all()
    return [docResponseDTO(r).to_dict() for r in registros]

def actualizar_doc(id, data):
    registro = Doc.query.get(id)
    if not registro:
        return {"error": "doc no encontrado"}
    
    dto = docRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEDOC", "DESDOC", "TIPDOC", "FECDOC", "IDEDOC", "DESDOC", "TIPDOC", "FECDOC"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "doc actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_doc(id):
    registro = Doc.query.get(id)
    if not registro:
        return {"error": "doc no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "doc eliminado correctamente"}
