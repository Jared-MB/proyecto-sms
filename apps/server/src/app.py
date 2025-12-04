from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os, uuid
from flask_migrate import Migrate
from config import BASE_STORAGE, API_TOKEN
from flask_cors import CORS
from models import db, Rep, Lug, Per, Emp, Coo, Car
from routes import registrar_endpoints


# ---------------------------------------------------------
# Configuración Flask y Base de Datos (MySQL)
# ---------------------------------------------------------

app = Flask(__name__)
CORS(app, 
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization"],
     expose_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
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


@app.route('/reportes', methods=['POST'])
def crear_reporte():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Extraer datos
    confidencial = data.get("con")
    fecsus = data.get("fecsus")
    fecrep = data.get("fecrep")
    lugsus = data.get("lugsus")
    obs = data.get("obs", "")
    freeve = data.get("freeve")
    emp = data.get("emp")

    # Validar campos requeridos (básico)
    if not all([confidencial, fecsus, fecrep, lugsus, freeve, emp]):
         return jsonify({"error": "Missing required fields"}), 400

    # Transformaciones
    obs = obs.upper() if obs else ""

    # Generar ID manual (replicando lógica PHP)
    # SELECT IDEREP FROM REP ORDER BY IDEREP DESC LIMIT 1
    last_rep = db.session.query(Rep).order_by(Rep.IDEREP.desc()).first()
    if last_rep:
        new_id = last_rep.IDEREP + 1
    else:
        new_id = 1

    # Crear nuevo objeto Rep
    new_rep = Rep(
        IDEREP=new_id,
        CONREP=int(confidencial),
        FECEVE=fecsus,  # Asumiendo formato correcto YYYY-MM-DD
        FECREP=fecrep,  # Asumiendo formato correcto YYYY-MM-DD HH:MM:SS
        FREREP=freeve,
        OBSREP=obs,
        LUGREP=int(lugsus),
        PERREP=int(emp),
        CANREP=0
    )

    try:
        db.session.add(new_rep)
        db.session.commit()
        return jsonify({
            "message": "Reporte creado exitosamente",
            "IDEREP": new_id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500




@app.route('/gestion/reportes', methods=['GET'])
def get_gestion_reportes():
    from models import Pel, Mon

    query = db.session.query(
        Rep.IDEREP,
        Rep.FECREP,
        Pel.FECPEL,
        Pel.NOMGESPEL,
        Pel.CONPEL,
        Pel.OBJPEL,
        Pel.ACTPEL,
        Pel.CATEPEL,
        Pel.GENPEL,
        Pel.METIDEPEL,
        Mon.ESTMON
    ).join(
        Pel, Rep.IDEREP == Pel.REPPEL
    ).join(
        Mon, Pel.REPPEL == Mon.PELMON
    )

    resultados = []
    for r in query.all():
        resultados.append({
            "IDEREP": r.IDEREP,
            "FECREP": r.FECREP,
            "FECPEL": r.FECPEL,
            "NOMGESPEL": r.NOMGESPEL,
            "CONPEL": r.CONPEL,
            "OBJPEL": r.OBJPEL,
            "ACTPEL": r.ACTPEL,
            "CATEPEL": r.CATEPEL,
            "GENPEL": r.GENPEL,
            "METIDEPEL": r.METIDEPEL,
            "ESTMON": r.ESTMON
        })

    return jsonify(resultados), 200


# ---------------------------------------------------------
# RUTAS DE ARCHIVOS (SIN CAMBIOS)
# ---------------------------------------------------------

@app.route('/lugares', methods=['GET'])
def get_lugares():
    lugares = Lug.query.all()
    return jsonify([{"IDELUG": l.IDELUG, "NOMLUG": l.NOMLUG} for l in lugares]), 200


@app.route('/coordinaciones', methods=['GET'])
def get_coordinaciones():
    areas = Coo.query.order_by(Coo.NOMCOO).all()
    return jsonify([{"IDECOO": a.IDECOO, "NOMCOO": a.NOMCOO} for a in areas]), 200


@app.route('/empleados', methods=['GET'])
def get_empleados():
    area_id = request.args.get('area')
    if not area_id:
        return jsonify([]), 200

    # Query replicating: SELECT IDEPER,NOMEMP,APPEMP,APMEMP FROM COO,CAR,EMP,PER ...
    query = db.session.query(Per.IDEPER, Emp.NOMEMP, Emp.APPEMP, Emp.APMEMP)\
        .join(Emp, Per.EMPPER == Emp.IDEEMP)\
        .join(Car, Per.CARPER == Car.IDECAR)\
        .join(Coo, Car.COOCAR == Coo.IDECOO)\
        .filter(Coo.IDECOO == area_id)

    resultados = []
    for row in query.all():
        resultados.append({
            "IDEPER": row.IDEPER,
            "NOMEMP": row.NOMEMP,
            "APPEMP": row.APPEMP,
            "APMEMP": row.APMEMP
        })
    
    return jsonify(resultados), 200


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
