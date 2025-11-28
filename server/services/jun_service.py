from models import db
from models import Jun
from services.util_service import convertirStringADate
from dto.jun_dto import JunRequestDTO, JunResponseDTO

def crear_jun(data):
    dto = JunRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Jun(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Jun creado correctamente"}

def leer_jun(id):
    registro = Jun.query.get(id)
    if not registro:
        return {"error": "Jun no encontrado"}
    return JunResponseDTO(registro).to_dict()

def leer_todos_jun():
    registros = Jun.query.all()
    return [JunResponseDTO(r).to_dict() for r in registros]

def actualizar_jun(id, data):
    registro = Jun.query.get(id)
    if not registro:
        return {"error": "Jun no encontrado"}
    
    dto = JunRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["idejun", "fecjun", "lugjun", "fefjun", "minjun", "diajun", "idejun", "fecjun", "lugjun", "fefjun", "minjun", "diajun"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Jun actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_jun(id):
    registro = Jun.query.get(id)
    if not registro:
        return {"error": "Jun no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Jun eliminado correctamente"}
