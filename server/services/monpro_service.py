from models import db
from models import Monpro
from services.util_service import convertirStringADate
from dto.monpro_dto import monproRequestDTO, monproResponseDTO

def crear_monpro(data):
    dto = monproRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Monpro(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "monpro creado correctamente"}

def leer_monpro(id):
    registro = Monpro.query.get(id)
    if not registro:
        return {"error": "monpro no encontrado"}
    return monproResponseDTO(registro).to_dict()

def leer_todos_monpro():
    registros = Monpro.query.all()
    return [monproResponseDTO(r).to_dict() for r in registros]

def actualizar_monpro(id, data):
    registro = Monpro.query.get(id)
    if not registro:
        return {"error": "monpro no encontrado"}
    
    dto = monproRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEMONPRO", "IDEMON", "IDEPRO", "IDEMONPRO", "IDEMON", "IDEPRO"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "monpro actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_monpro(id):
    registro = Monpro.query.get(id)
    if not registro:
        return {"error": "monpro no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "monpro eliminado correctamente"}
