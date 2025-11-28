from models import db
from models import Nor
from services.util_service import convertirStringADate
from dto.nor_dto import NorRequestDTO, NorResponseDTO

def crear_nor(data):
    dto = NorRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Nor(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Nor creado correctamente"}

def leer_nor(id):
    registro = Nor.query.get(id)
    if not registro:
        return {"error": "Nor no encontrado"}
    return NorResponseDTO(registro).to_dict()

def leer_todos_nor():
    registros = Nor.query.all()
    return [NorResponseDTO(r).to_dict() for r in registros]

def actualizar_nor(id, data):
    registro = Nor.query.get(id)
    if not registro:
        return {"error": "Nor no encontrado"}
    
    dto = NorRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDENOR", "NOMNOR", "NORTPO", "IDENOR", "NOMNOR", "NORTPO"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Nor actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_nor(id):
    registro = Nor.query.get(id)
    if not registro:
        return {"error": "Nor no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Nor eliminado correctamente"}
