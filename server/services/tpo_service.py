from models import db
from models import Tpo
from services.util_service import convertirStringADate
from dto.tpo_dto import TpoRequestDTO, TpoResponseDTO

def crear_tpo(data):
    dto = TpoRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Tpo(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Tpo creado correctamente"}

def leer_tpo(id):
    registro = Tpo.query.get(id)
    if not registro:
        return {"error": "Tpo no encontrado"}
    return TpoResponseDTO(registro).to_dict()

def leer_todos_tpo():
    registros = Tpo.query.all()
    return [TpoResponseDTO(r).to_dict() for r in registros]

def actualizar_tpo(id, data):
    registro = Tpo.query.get(id)
    if not registro:
        return {"error": "Tpo no encontrado"}
    
    dto = TpoRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDETPO", "NOMTPO", "TCATPO", "IDETPO", "NOMTPO", "TCATPO"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Tpo actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_tpo(id):
    registro = Tpo.query.get(id)
    if not registro:
        return {"error": "Tpo no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Tpo eliminado correctamente"}
