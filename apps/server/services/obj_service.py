from models import db
from models import Obj
from services.util_service import convertirStringADate
from dto.obj_dto import ObjRequestDTO, ObjResponseDTO

def crear_obj(data):
    dto = ObjRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Obj(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Obj creado correctamente"}

def leer_obj(id):
    registro = Obj.query.get(id)
    if not registro:
        return {"error": "Obj no encontrado"}
    return ObjResponseDTO(registro).to_dict()

def leer_todos_obj():
    registros = Obj.query.all()
    return [ObjResponseDTO(r).to_dict() for r in registros]

def actualizar_obj(id, data):
    registro = Obj.query.get(id)
    if not registro:
        return {"error": "Obj no encontrado"}
    
    dto = ObjRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEOBJ", "TIPOBJ", "OBJCAP", "DESOBJ", "IDEOBJ", "TIPOBJ", "OBJCAP", "DESOBJ"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Obj actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_obj(id):
    registro = Obj.query.get(id)
    if not registro:
        return {"error": "Obj no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Obj eliminado correctamente"}
