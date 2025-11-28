from models import db
from models import Tac
from services.util_service import convertirStringADate
from dto.tac_dto import TacRequestDTO, TacResponseDTO

def crear_tac(data):
    dto = TacRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Tac(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Tac creado correctamente"}

def leer_tac(id):
    registro = Tac.query.get(id)
    if not registro:
        return {"error": "Tac no encontrado"}
    return TacResponseDTO(registro).to_dict()

def leer_todos_tac():
    registros = Tac.query.all()
    return [TacResponseDTO(r).to_dict() for r in registros]

def actualizar_tac(id, data):
    registro = Tac.query.get(id)
    if not registro:
        return {"error": "Tac no encontrado"}
    
    dto = TacRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDETAC", "DESTAC", "TACTOP", "IDETAC", "DESTAC", "TACTOP"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Tac actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_tac(id):
    registro = Tac.query.get(id)
    if not registro:
        return {"error": "Tac no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Tac eliminado correctamente"}
