from models import db
from models import Con
from services.util_service import convertirStringADate
from dto.con_dto import ConRequestDTO, ConResponseDTO

def crear_con(data):
    dto = ConRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Con(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Con creado correctamente"}

def leer_con(id):
    registro = Con.query.get(id)
    if not registro:
        return {"error": "Con no encontrado"}
    return ConResponseDTO(registro).to_dict()

def leer_todos_con():
    registros = Con.query.all()
    return [ConResponseDTO(r).to_dict() for r in registros]

def actualizar_con(id, data):
    registro = Con.query.get(id)
    if not registro:
        return {"error": "Con no encontrado"}
    
    dto = ConRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["idecon", "nomcon", "descon", "tipcon", "idecon", "nomcon", "descon", "tipcon"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Con actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_con(id):
    registro = Con.query.get(id)
    if not registro:
        return {"error": "Con no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Con eliminado correctamente"}
