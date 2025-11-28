from models import db
from models import Ext
from services.util_service import convertirStringADate
from dto.ext_dto import ExtRequestDTO, ExtResponseDTO

def crear_ext(data):
    dto = ExtRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Ext(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Ext creado correctamente"}

def leer_ext(id):
    registro = Ext.query.get(id)
    if not registro:
        return {"error": "Ext no encontrado"}
    return ExtResponseDTO(registro).to_dict()

def leer_todos_ext():
    registros = Ext.query.all()
    return [ExtResponseDTO(r).to_dict() for r in registros]

def actualizar_ext(id, data):
    registro = Ext.query.get(id)
    if not registro:
        return {"error": "Ext no encontrado"}
    
    dto = ExtRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDEEXT", "APCEXT", "AMCEXT", "NMCEXT", "TEMEXT", "EXTCAP", "EXTORG", "IDEEXT", "APCEXT", "AMCEXT", "NMCEXT", "TEMEXT", "EXTCAP", "EXTORG"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Ext actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_ext(id):
    registro = Ext.query.get(id)
    if not registro:
        return {"error": "Ext no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Ext eliminado correctamente"}
