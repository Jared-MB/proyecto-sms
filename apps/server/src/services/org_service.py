from models import db
from models import Org
from services.util_service import convertirStringADate
from dto.org_dto import OrgRequestDTO, OrgResponseDTO

def crear_org(data):
    dto = OrgRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Org(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Org creado correctamente"}

def leer_org(id):
    registro = Org.query.get(id)
    if not registro:
        return {"error": "Org no encontrado"}
    return OrgResponseDTO(registro).to_dict()

def leer_todos_org():
    registros = Org.query.all()
    return [OrgResponseDTO(r).to_dict() for r in registros]

def actualizar_org(id, data):
    registro = Org.query.get(id)
    if not registro:
        return {"error": "Org no encontrado"}
    
    dto = OrgRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEORG", "NOMORG", "DIRORG", "TELORG", "IDEORG", "NOMORG", "DIRORG", "TELORG"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Org actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_org(id):
    registro = Org.query.get(id)
    if not registro:
        return {"error": "Org no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Org eliminado correctamente"}
