import os
import re

# === CONFIGURACIÓN ===
dto_dir = "dto"
output_dir = "services"
os.makedirs(output_dir, exist_ok=True)

# === FUNCIÓN PARA OBTENER LOS NOMBRES DE MODELOS ===
def obtener_modelos_desde_dto(carpeta):
    modelos = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith("_dto.py"):
            ruta = os.path.join(carpeta, archivo)
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
            match = re.search(r"class\s+(\w+)RequestDTO", contenido)
            if match:
                modelo = match.group(1)
                modelos.append(modelo)
    return modelos

# === PLANTILLA BASE ACTUALIZADA ===
template = '''from models import db
from models import {model_capitalize}
from services.util_service import convertirStringADate
from dto.{model_lower}_dto import {model}RequestDTO, {model}ResponseDTO

def crear_{model_lower}(data):
    dto = {model}RequestDTO(data)
    data = dto.to_dict()
    for k, v in data.items():
        if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
            data[k] = convertirStringADate(v)
    registro = {model_capitalize}(**data)
    db.session.add(registro)
    db.session.commit()
    return {{"mensaje": "{model} creado correctamente"}}

def leer_{model_lower}(id):
    registro = {model_capitalize}.query.get(id)
    if not registro:
        return {{"error": "{model} no encontrado"}}
    return {model}ResponseDTO(registro).to_dict()

def leer_todos_{model_lower}():
    registros = {model_capitalize}.query.all()
    return [{model}ResponseDTO(r).to_dict() for r in registros]

def actualizar_{model_lower}(id, data):
    registro = {model_capitalize}.query.get(id)
    if not registro:
        return {{"error": "{model} no encontrado"}}
    
    dto = {model}RequestDTO(data)
    data = dto.to_dict()

    # === SOLO CAMPOS VALIDOS ===
    campos_validos = [{campos_validos}]
    for k in campos_validos:
        if k in data:
            v = data[k]
            if isinstance(v, str) and ("fec" in k.lower() or "nac" in k.lower()):
                v = convertirStringADate(v)
            setattr(registro, k, v)

    try:
        db.session.commit()
        return {{"mensaje": "{model} actualizado correctamente"}}
    except Exception as e:
        db.session.rollback()
        return {{"error": str(e)}}

def borrar_{model_lower}(id):
    registro = {model_capitalize}.query.get(id)
    if not registro:
        return {{"error": "{model} no encontrado"}}
    db.session.delete(registro)
    db.session.commit()
    return {{"mensaje": "{model} eliminado correctamente"}}
'''

# === PROCESO ===
modelos = obtener_modelos_desde_dto(dto_dir)

if not modelos:
    print("No se encontraron DTOs en la carpeta /dto")
else:
    print(f"Se detectaron {len(modelos)} modelos: {', '.join(modelos)}")

for model in modelos:
    model_lower = model.lower()
    model_capitalize = model.capitalize()
    
    # === EXTRAER CAMPOS VALIDOS DESDE EL DTO ===
    dto_file = os.path.join(dto_dir, f"{model_lower}_dto.py")
    campos_validos = []
    with open(dto_file, "r", encoding="utf-8") as f:
        contenido = f.read()
    for match in re.findall(r"self\.(\w+)\s*=", contenido):
        if match.lower() != "id":  # excluye 'id'
            campos_validos.append(f'"{match}"')
    campos_validos_str = ", ".join(campos_validos)
    
    # === GENERAR ARCHIVO DE SERVICIO ===
    file_path = os.path.join(output_dir, f"{model_lower}_service.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(template.format(
            model=model,
            model_lower=model_lower,
            model_capitalize=model_capitalize,
            campos_validos=campos_validos_str
        ))
    print(f"{file_path} generado correctamente.")
