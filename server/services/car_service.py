from models import db
from models import Car
from services.util_service import convertirStringADate
from dto.car_dto import CarRequestDTO, CarResponseDTO

def crear_car(data):
    dto = CarRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Car(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Car creado correctamente"}

def leer_car(id):
    registro = Car.query.get(id)
    if not registro:
        return {"error": "Car no encontrado"}
    return CarResponseDTO(registro).to_dict()

def leer_todos_car():
    registros = Car.query.all()
    return [CarResponseDTO(r).to_dict() for r in registros]

def actualizar_car(id, data):
    registro = Car.query.get(id)
    if not registro:
        return {"error": "Car no encontrado"}
    
    dto = CarRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["IDECAR", "NOMCAR", "COOCAR", "CARCAR", "ORGCAR", "IDECAR", "NOMCAR", "COOCAR", "CARCAR", "ORGCAR"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Car actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_car(id):
    registro = Car.query.get(id)
    if not registro:
        return {"error": "Car no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Car eliminado correctamente"}
