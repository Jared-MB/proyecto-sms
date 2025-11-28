from models import db
from models import Cic
from services.util_service import convertirStringADate
from dto.cic_dto import cicRequestDTO, cicResponseDTO

def crear_cic(data):
    dto = cicRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Cic(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "cic creado correctamente"}

def leer_cic(id):
    registro = Cic.query.get(id)
    if not registro:
        return {"error": "cic no encontrado"}
    return cicResponseDTO(registro).to_dict()

def leer_todos_cic():
    registros = Cic.query.all()
    return [cicResponseDTO(r).to_dict() for r in registros]

def actualizar_cic(id, data):
    registro = Cic.query.get(id)
    if not registro:
        return {"error": "cic no encontrado"}
    
    dto = cicRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDECIC", "DESCIC", "FECCIC", "IDECIC", "DESCIC", "FECCIC"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "cic actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_cic(id):
    registro = Cic.query.get(id)
    if not registro:
        return {"error": "cic no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "cic eliminado correctamente"}
