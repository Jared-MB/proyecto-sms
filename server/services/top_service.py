from models import db
from models import Top
from services.util_service import convertirStringADate
from dto.top_dto import TopRequestDTO, TopResponseDTO

def crear_top(data):
    dto = TopRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Top(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Top creado correctamente"}

def leer_top(id):
    registro = Top.query.get(id)
    if not registro:
        return {"error": "Top no encontrado"}
    return TopResponseDTO(registro).to_dict()

def leer_todos_top():
    registros = Top.query.all()
    return [TopResponseDTO(r).to_dict() for r in registros]

def actualizar_top(id, data):
    registro = Top.query.get(id)
    if not registro:
        return {"error": "Top no encontrado"}
    
    dto = TopRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDETOP", "NMTTOP", "DESTOP", "IDETOP", "NMTTOP", "DESTOP"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Top actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_top(id):
    registro = Top.query.get(id)
    if not registro:
        return {"error": "Top no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Top eliminado correctamente"}
