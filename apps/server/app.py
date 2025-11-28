from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os, uuid
from flask_migrate import Migrate
from config import BASE_STORAGE, API_TOKEN
from flask_cors import CORS
from models import db, Rep, Lug, Per, Emp   # <-- AÑADIDO Per
from routes import registrar_endpoints


# ---------------------------------------------------------
# Configuración Flask y Base de Datos (MySQL)
# ---------------------------------------------------------

app = Flask(__name__)
CORS(app, supports_credentials=True)
registrar_endpoints(app)

# MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/sms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


# ---------------------------------------------------------
# Validación del token
# ---------------------------------------------------------
def validar_token():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return False
    token = auth_header.split("Bearer ")[-1]
    return token == API_TOKEN


@app.before_request
def before_request():
    if request.method == "OPTIONS":
        return '', 200

    if request.endpoint in ['download', 'home']:
        return

    if not validar_token():
        return jsonify({"error": "Unauthorized"}), 401


# ---------------------------------------------------------
# SERVICIO COMBINADO (Rep + Lug + Per + Emp)
# ---------------------------------------------------------
@app.route('/reportes-completo/<int:user_id>', methods=['GET'])
def reportes_completo_por_usuario(user_id):

    query = db.session.query(
        Rep.IDEREP,
        Rep.FECREP,
        Rep.FECEVE,
        Rep.FREREP,
        Rep.OBSREP,
        Rep.CANREP,
        Lug.NOMLUG,
        Emp.NOMEMP,
        Emp.APPEMP,
        Emp.APMEMP
    ).join(
        Lug, Rep.LUGREP == Lug.IDELUG
    ).join(
        Per, Rep.PERREP == Per.IDEPER
    ).join(
        Emp, Per.EMPPER == Emp.IDEEMP
    ).order_by(
        Rep.IDEREP.asc()
    )

    resultados = []
    for r in query.all():
        resultados.append({
            "IDEREP": r.IDEREP,
            "FECREP": r.FECREP,
            "FECEVE": r.FECEVE,
            "FREREP": r.FREREP,
            "OBSREP": r.OBSREP,
            "CANREP": r.CANREP,
            "NOMLUG": r.NOMLUG,
            "NOMEMP": r.NOMEMP,
            "APPEMP": r.APPEMP,
            "APMEMP": r.APMEMP,
        })

    return jsonify(resultados), 200


# ---------------------------------------------------------
# RUTAS DE ARCHIVOS (SIN CAMBIOS)
# ---------------------------------------------------------

@app.route('/upload', methods=['POST'])
def upload():
    user_id = request.form.get('user_id')
    file = request.files.get('file') or request.files.get('evi')

    if not user_id or not file:
        return jsonify({"error": "Faltan parámetros"}), 400

    user_dir = os.path.join(BASE_STORAGE, user_id)
    os.makedirs(user_dir, exist_ok=True)

    nombre_seguro = secure_filename(file.filename)
    nuevo_nombre = f"{uuid.uuid4()}_{nombre_seguro}"
    ruta = os.path.join(user_dir, nuevo_nombre)
    file.save(ruta)

    return jsonify({
        "message": "Archivo guardado correctamente",
        "file_name": nuevo_nombre
    }), 200


@app.route('/list/<user_id>', methods=['GET'])
def listar(user_id):
    user_dir = os.path.join(BASE_STORAGE, user_id)
    if not os.path.exists(user_dir):
        return jsonify([])

    archivos = os.listdir(user_dir)
    return jsonify(archivos), 200

@app.route('/file/<user_id>/<filename>', methods=['GET'])
def download(user_id, filename):
    ruta = os.path.join(BASE_STORAGE, user_id, filename)
    if not os.path.exists(ruta):
        return jsonify({"error": "Archivo no encontrado"}), 404
    return send_file(ruta, as_attachment=True)


@app.route('/file/<user_id>/<filename>', methods=['DELETE'])
def delete(user_id, filename):
    ruta = os.path.join(BASE_STORAGE, user_id, filename)
    if os.path.exists(ruta):
        os.remove(ruta)
        return jsonify({"message": "Archivo eliminado"}), 200
    return jsonify({"error": "No existe el archivo"}), 404


@app.route('/')
def home():
    return "Servicio de almacenamiento activo"


if __name__ == '__main__':
    os.makedirs(BASE_STORAGE, exist_ok=True)
    app.run(host='127.0.0.1', port=5001, debug=True)
