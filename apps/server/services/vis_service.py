from models import db
from models import Vis
from services.util_service import convertirStringADate
from dto.vis_dto import visRequestDTO, visResponseDTO

def crear_vis(data):
    dto = visRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Vis(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "vis creado correctamente"}

def leer_vis(id):
    registro = Vis.query.get(id)
    if not registro:
        return {"error": "vis no encontrado"}
    return visResponseDTO(registro).to_dict()

def leer_todos_vis():
    registros = Vis.query.all()
    return [visResponseDTO(r).to_dict() for r in registros]

def actualizar_vis(id, data):
    registro = Vis.query.get(id)
    if not registro:
        return {"error": "vis no encontrado"}
    
    dto = visRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEVIS", "PUBVIS", "EMCVIS", "FECVIS", "IDEVIS", "PUBVIS", "EMCVIS", "FECVIS"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "vis actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_vis(id):
    registro = Vis.query.get(id)
    if not registro:
        return {"error": "vis no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "vis eliminado correctamente"}
