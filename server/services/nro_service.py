from models import db
from models import Nro
from services.util_service import convertirStringADate
from dto.nro_dto import NroRequestDTO, NroResponseDTO

def crear_nro(data):
    dto = NroRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Nro(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Nro creado correctamente"}

def leer_nro(id):
    registro = Nro.query.get(id)
    if not registro:
        return {"error": "Nro no encontrado"}
    return NroResponseDTO(registro).to_dict()

def leer_todos_nro():
    registros = Nro.query.all()
    return [NroResponseDTO(r).to_dict() for r in registros]

def actualizar_nro(id, data):
    registro = Nro.query.get(id)
    if not registro:
        return {"error": "Nro no encontrado"}
    
    dto = NroRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDENRO", "NOMNRO", "NROCAP", "IDENRO", "NOMNRO", "NROCAP"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Nro actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_nro(id):
    registro = Nro.query.get(id)
    if not registro:
        return {"error": "Nro no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Nro eliminado correctamente"}
