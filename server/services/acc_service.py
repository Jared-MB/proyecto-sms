from models import db
from models import Acc
from services.util_service import convertirStringADate
from dto.acc_dto import accRequestDTO, accResponseDTO

def crear_acc(data):
    dto = accRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Acc(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "acc creado correctamente"}

def leer_acc(id):
    registro = Acc.query.get(id)
    if not registro:
        return {"error": "acc no encontrado"}
    return accResponseDTO(registro).to_dict()

def leer_todos_acc():
    registros = Acc.query.all()
    return [accResponseDTO(r).to_dict() for r in registros]

def actualizar_acc(id, data):
    registro = Acc.query.get(id)
    if not registro:
        return {"error": "acc no encontrado"}
    
    dto = accRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEACC", "DESACC", "RESACC", "FECACC", "IDEACC", "DESACC", "RESACC", "FECACC"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "acc actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_acc(id):
    registro = Acc.query.get(id)
    if not registro:
        return {"error": "acc no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "acc eliminado correctamente"}
