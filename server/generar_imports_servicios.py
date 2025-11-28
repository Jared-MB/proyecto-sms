import os
import re

# === CONFIGURACIÓN ===
services_dir = "services"
output_file = os.path.join(services_dir, "__init__.py")

# === OBTENER ARCHIVOS DE SERVICIO ===
def obtener_servicios(carpeta):
    servicios = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith("_service.py") and archivo != "util_service.py":
            servicio = archivo.replace("_service.py", "")
            servicios.append(servicio)
    return servicios

# === GENERAR IMPORTS ===
def generar_imports(servicios):
    imports = []
    for servicio in servicios:
        nombre_modelo = servicio  # ejemplo: "rep", "emp", "lug"

        linea = (
            f"from services.{servicio}_service import (\n"
            f"    crear_{nombre_modelo},\n"
            f"    leer_{nombre_modelo},\n"
            f"    leer_todos_{nombre_modelo},\n"
            f"    actualizar_{nombre_modelo},\n"
            f"    borrar_{nombre_modelo}\n"
            f")"
        )

        imports.append(linea)

    # Agregar util_service si existe
    if os.path.exists(os.path.join(services_dir, "util_service.py")):
        imports.append(
            "\nfrom services.util_service import (\n"
            "    obtenerUbicacionIP,\n"
            "    limpiarTextoIA\n"
            ")"
        )

    return "\n\n".join(imports)

# === GENERAR ARCHIVO FINAL ===
def main():
    servicios = obtener_servicios(services_dir)
    
    if not servicios:
        print("⚠️ No se encontraron servicios en la carpeta /services")
        return

    contenido = generar_imports(servicios)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(contenido)

    print(f"✅ Archivo __init__.py generado correctamente")
    print("📦 Servicios detectados:", ", ".join(servicios))


if __name__ == "__main__":
    main()
