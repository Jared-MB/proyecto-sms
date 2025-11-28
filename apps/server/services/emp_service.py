from models import db
from models import Emp
from services.util_service import convertirStringADate
from dto.emp_dto import EmpRequestDTO, EmpResponseDTO

def crear_emp(data):
    dto = EmpRequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = Emp(**data)
    db.session.add(registro)
    db.session.commit()
    return {"mensaje": "Emp creado correctamente"}

def leer_emp(id):
    registro = Emp.query.get(id)
    if not registro:
        return {"error": "Emp no encontrado"}
    return EmpResponseDTO(registro).to_dict()

def leer_todos_emp():
    registros = Emp.query.all()
    return [EmpResponseDTO(r).to_dict() for r in registros]

def actualizar_emp(id, data):
    registro = Emp.query.get(id)
    if not registro:
        return {"error": "Emp no encontrado"}
    
    dto = EmpRequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = ["ideemp", "appemp", "apmemp", "nomemp", "emaemp", "celemp", "cel2emp", "telofiemp", "telofi2emp", "extemp", "fotemp", "ideemp", "appemp", "apmemp", "nomemp", "emaemp", "celemp", "cel2emp", "telofiemp", "telofi2emp", "extemp", "fotemp"]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {"mensaje": "Emp actualizado correctamente"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def borrar_emp(id):
    registro = Emp.query.get(id)
    if not registro:
        return {"error": "Emp no encontrado"}
    db.session.delete(registro)
    db.session.commit()
    return {"mensaje": "Emp eliminado correctamente"}
