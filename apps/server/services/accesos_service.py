from models import db
from models import Accesos
from services.util_service import convertirStringADate
from dto.accesos_dto import AccesosRequestDTO, AccesosResponseDTO

def crear_accesos(data):
    dto = AccesosRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Accesos(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Accesos creado correctamente"}

def leer_accesos(id):
    registro = Accesos.query.get(id)
    if not registro:
        return {"error": "Accesos no encontrado"}
    return AccesosResponseDTO(registro).to_dict()

def leer_todos_accesos():
    registros = Accesos.query.all()
    return [AccesosResponseDTO(r).to_dict() for r in registros]

def actualizar_accesos(id, data):
    registro = Accesos.query.get(id)
    if not registro:
        return {"error": "Accesos no encontrado"}
    
    dto = AccesosRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["ideacc", "diracc", "fecacc", "broacc", "useacc", "ideacc", "diracc", "fecacc", "broacc", "useacc"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Accesos actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_accesos(id):
    registro = Accesos.query.get(id)
    if not registro:
        return {"error": "Accesos no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Accesos eliminado correctamente"}
