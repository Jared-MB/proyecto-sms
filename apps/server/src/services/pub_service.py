from models import db
from models import Pub
from services.util_service import convertirStringADate
from dto.pub_dto import PubRequestDTO, PubResponseDTO

def crear_pub(data):
    dto = PubRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Pub(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Pub creado correctamente"}

def leer_pub(id):
    registro = Pub.query.get(id)
    if not registro:
        return {"error": "Pub no encontrado"}
    return PubResponseDTO(registro).to_dict()

def leer_todos_pub():
    registros = Pub.query.all()
    return [PubResponseDTO(r).to_dict() for r in registros]

def actualizar_pub(id, data):
    registro = Pub.query.get(id)
    if not registro:
        return {"error": "Pub no encontrado"}
    
    dto = PubRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEPUB", "FECPUB", "NOMPUB", "NOPPUB", "MEDPUB", "CONPUB", "DOCPUB", "IDEPUB", "FECPUB", "NOMPUB", "NOPPUB", "MEDPUB", "CONPUB", "DOCPUB"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Pub actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_pub(id):
    registro = Pub.query.get(id)
    if not registro:
        return {"error": "Pub no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Pub eliminado correctamente"}
