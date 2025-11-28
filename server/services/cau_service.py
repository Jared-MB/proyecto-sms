from models import db
from models import Cau
from services.util_service import convertirStringADate
from dto.cau_dto import cauRequestDTO, cauResponseDTO

def crear_cau(data):
    dto = cauRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Cau(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "cau creado correctamente"}

def leer_cau(id):
    registro = Cau.query.get(id)
    if not registro:
        return {"error": "cau no encontrado"}
    return cauResponseDTO(registro).to_dict()

def leer_todos_cau():
    registros = Cau.query.all()
    return [cauResponseDTO(r).to_dict() for r in registros]

def actualizar_cau(id, data):
    registro = Cau.query.get(id)
    if not registro:
        return {"error": "cau no encontrado"}
    
    dto = cauRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDECAU", "DESCAU", "TIPCAU", "IDECAU", "DESCAU", "TIPCAU"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "cau actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_cau(id):
    registro = Cau.query.get(id)
    if not registro:
        return {"error": "cau no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "cau eliminado correctamente"}
