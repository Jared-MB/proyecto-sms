from models import db
from models import Val
from services.util_service import convertirStringADate
from dto.val_dto import valRequestDTO, valResponseDTO

def crear_val(data):
    dto = valRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Val(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "val creado correctamente"}

def leer_val(id):
    registro = Val.query.get(id)
    if not registro:
        return {"error": "val no encontrado"}
    return valResponseDTO(registro).to_dict()

def leer_todos_val():
    registros = Val.query.all()
    return [valResponseDTO(r).to_dict() for r in registros]

def actualizar_val(id, data):
    registro = Val.query.get(id)
    if not registro:
        return {"error": "val no encontrado"}
    
    dto = valRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEVAL", "PERVAL", "DIAVAL", "HORINI", "FECVAL", "CALVAL", "DIAEXT", "IDEVAL", "PERVAL", "DIAVAL", "HORINI", "FECVAL", "CALVAL", "DIAEXT"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "val actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_val(id):
    registro = Val.query.get(id)
    if not registro:
        return {"error": "val no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "val eliminado correctamente"}
