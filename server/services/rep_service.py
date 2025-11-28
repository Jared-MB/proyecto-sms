from models import db
from models import Rep
from services.util_service import convertirStringADate
from dto.rep_dto import repRequestDTO, repResponseDTO

def crear_rep(data):
    dto = repRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Rep(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "rep creado correctamente"}

def leer_rep(id):
    registro = Rep.query.get(id)
    if not registro:
        return {"error": "rep no encontrado"}
    return repResponseDTO(registro).to_dict()

def leer_todos_rep():
    registros = Rep.query.all()
    return [repResponseDTO(r).to_dict() for r in registros]

def actualizar_rep(id, data):
    registro = Rep.query.get(id)
    if not registro:
        return {"error": "rep no encontrado"}
    
    dto = repRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEREP", "CONREP", "FECEVE", "FECREP", "FREREP", "LUGREP", "CANREP", "PERREP", "OBSREP", "IDEREP", "CONREP", "FECEVE", "FECREP", "FREREP", "LUGREP", "CANREP", "PERREP", "OBSREP"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "rep actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_rep(id):
    registro = Rep.query.get(id)
    if not registro:
        return {"error": "rep no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "rep eliminado correctamente"}
