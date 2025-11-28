from models import db
from models import Coo
from services.util_service import convertirStringADate
from dto.coo_dto import CooRequestDTO, CooResponseDTO

def crear_coo(data):
    dto = CooRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Coo(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Coo creado correctamente"}

def leer_coo(id):
    registro = Coo.query.get(id)
    if not registro:
        return {"error": "Coo no encontrado"}
    return CooResponseDTO(registro).to_dict()

def leer_todos_coo():
    registros = Coo.query.all()
    return [CooResponseDTO(r).to_dict() for r in registros]

def actualizar_coo(id, data):
    registro = Coo.query.get(id)
    if not registro:
        return {"error": "Coo no encontrado"}
    
    dto = CooRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["idecoo", "nomcoo", "idecoo", "nomcoo"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Coo actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_coo(id):
    registro = Coo.query.get(id)
    if not registro:
        return {"error": "Coo no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Coo eliminado correctamente"}
