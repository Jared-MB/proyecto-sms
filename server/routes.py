from flask import jsonify, request

# === IMPORTAR TODOS LOS SERVICIOS (incluye leer_todos_xxx) ===
from services.acc_service import crear_acc, leer_acc, leer_todos_acc, actualizar_acc, borrar_acc
from services.bib_service import crear_bib, leer_bib, leer_todos_bib, actualizar_bib, borrar_bib
from services.cap_service import crear_cap, leer_cap, leer_todos_cap, actualizar_cap, borrar_cap
from services.car_service import crear_car, leer_car, leer_todos_car, actualizar_car, borrar_car
from services.cau_service import crear_cau, leer_cau, leer_todos_cau, actualizar_cau, borrar_cau
from services.cic_service import crear_cic, leer_cic, leer_todos_cic, actualizar_cic, borrar_cic
from services.com_service import crear_com, leer_com, leer_todos_com, actualizar_com, borrar_com
from services.con_service import crear_con, leer_con, leer_todos_con, actualizar_con, borrar_con
from services.coo_service import crear_coo, leer_coo, leer_todos_coo, actualizar_coo, borrar_coo
from services.dia_service import crear_dia, leer_dia, leer_todos_dia, actualizar_dia, borrar_dia
from services.docmon_service import crear_docmon, leer_docmon, leer_todos_docmon, actualizar_docmon, borrar_docmon
from services.doc_service import crear_doc, leer_doc, leer_todos_doc, actualizar_doc, borrar_doc
from services.ejm_service import crear_ejm, leer_ejm, leer_todos_ejm, actualizar_ejm, borrar_ejm
from services.emp_service import crear_emp, leer_emp, leer_todos_emp, actualizar_emp, borrar_emp
from services.evi_service import crear_evi, leer_evi, leer_todos_evi, actualizar_evi, borrar_evi
from services.ext_service import crear_ext, leer_ext, leer_todos_ext, actualizar_ext, borrar_ext
from services.jun_service import crear_jun, leer_jun, leer_todos_jun, actualizar_jun, borrar_jun
from services.lug_service import crear_lug, leer_lug, leer_todos_lug, actualizar_lug, borrar_lug
from services.med_service import crear_med, leer_med, leer_todos_med, actualizar_med, borrar_med
from services.monpro_service import crear_monpro, leer_monpro, leer_todos_monpro, actualizar_monpro, borrar_monpro
from services.mon_service import crear_mon, leer_mon, leer_todos_mon, actualizar_mon, borrar_mon
from services.nec_service import crear_nec, leer_nec, leer_todos_nec, actualizar_nec, borrar_nec
from services.nor_service import crear_nor, leer_nor, leer_todos_nor, actualizar_nor, borrar_nor
from services.nro_service import crear_nro, leer_nro, leer_todos_nro, actualizar_nro, borrar_nro
from services.obj_service import crear_obj, leer_obj, leer_todos_obj, actualizar_obj, borrar_obj
from services.org_service import crear_org, leer_org, leer_todos_org, actualizar_org, borrar_org
from services.pel_service import crear_pel, leer_pel, leer_todos_pel, actualizar_pel, borrar_pel
from services.per_service import crear_per, leer_per, leer_todos_per, actualizar_per, borrar_per
from services.pri_service import crear_pri, leer_pri, leer_todos_pri, actualizar_pri, borrar_pri
from services.projc_service import crear_projc, leer_projc, leer_todos_projc, actualizar_projc, borrar_projc
from services.pro_service import crear_pro, leer_pro, leer_todos_pro, actualizar_pro, borrar_pro
from services.pub_service import crear_pub, leer_pub, leer_todos_pub, actualizar_pub, borrar_pub
from services.rep_service import crear_rep, leer_rep, leer_todos_rep, actualizar_rep, borrar_rep
from services.res_service import crear_res, leer_res, leer_todos_res, actualizar_res, borrar_res
from services.rie_service import crear_rie, leer_rie, leer_todos_rie, actualizar_rie, borrar_rie
from services.ses_service import crear_ses, leer_ses, leer_todos_ses, actualizar_ses, borrar_ses
from services.sugerencias_service import crear_sugerencias, leer_sugerencias, leer_todos_sugerencias, actualizar_sugerencias, borrar_sugerencias
from services.tac_service import crear_tac, leer_tac, leer_todos_tac, actualizar_tac, borrar_tac
from services.teccap_service import crear_teccap, leer_teccap, leer_todos_teccap, actualizar_teccap, borrar_teccap
from services.tec_service import crear_tec, leer_tec, leer_todos_tec, actualizar_tec, borrar_tec
from services.temjc_service import crear_temjc, leer_temjc, leer_todos_temjc, actualizar_temjc, borrar_temjc
from services.tem_service import crear_tem, leer_tem, leer_todos_tem, actualizar_tem, borrar_tem
from services.ten_service import crear_ten, leer_ten, leer_todos_ten, actualizar_ten, borrar_ten
from services.top_service import crear_top, leer_top, leer_todos_top, actualizar_top, borrar_top
from services.tpo_service import crear_tpo, leer_tpo, leer_todos_tpo, actualizar_tpo, borrar_tpo
from services.val_service import crear_val, leer_val, leer_todos_val, actualizar_val, borrar_val
from services.vis_service import crear_vis, leer_vis, leer_todos_vis, actualizar_vis, borrar_vis


def registrar_endpoints(app):
    """
    Registra automáticamente los endpoints CRUD + LEER_TODOS de todos los servicios.
    """
    servicios = {
        'acc': (crear_acc, leer_acc, leer_todos_acc, actualizar_acc, borrar_acc),
        'bib': (crear_bib, leer_bib, leer_todos_bib, actualizar_bib, borrar_bib),
        'cap': (crear_cap, leer_cap, leer_todos_cap, actualizar_cap, borrar_cap),
        'car': (crear_car, leer_car, leer_todos_car, actualizar_car, borrar_car),
        'cau': (crear_cau, leer_cau, leer_todos_cau, actualizar_cau, borrar_cau),
        'cic': (crear_cic, leer_cic, leer_todos_cic, actualizar_cic, borrar_cic),
        'com': (crear_com, leer_com, leer_todos_com, actualizar_com, borrar_com),
        'con': (crear_con, leer_con, leer_todos_con, actualizar_con, borrar_con),
        'coo': (crear_coo, leer_coo, leer_todos_coo, actualizar_coo, borrar_coo),
        'dia': (crear_dia, leer_dia, leer_todos_dia, actualizar_dia, borrar_dia),
        'docmon': (crear_docmon, leer_docmon, leer_todos_docmon, actualizar_docmon, borrar_docmon),
        'doc': (crear_doc, leer_doc, leer_todos_doc, actualizar_doc, borrar_doc),
        'ejm': (crear_ejm, leer_ejm, leer_todos_ejm, actualizar_ejm, borrar_ejm),
        'emp': (crear_emp, leer_emp, leer_todos_emp, actualizar_emp, borrar_emp),
        'evi': (crear_evi, leer_evi, leer_todos_evi, actualizar_evi, borrar_evi),
        'ext': (crear_ext, leer_ext, leer_todos_ext, actualizar_ext, borrar_ext),
        'jun': (crear_jun, leer_jun, leer_todos_jun, actualizar_jun, borrar_jun),
        'lug': (crear_lug, leer_lug, leer_todos_lug, actualizar_lug, borrar_lug),
        'med': (crear_med, leer_med, leer_todos_med, actualizar_med, borrar_med),
        'monpro': (crear_monpro, leer_monpro, leer_todos_monpro, actualizar_monpro, borrar_monpro),
        'mon': (crear_mon, leer_mon, leer_todos_mon, actualizar_mon, borrar_mon),
        'nec': (crear_nec, leer_nec, leer_todos_nec, actualizar_nec, borrar_nec),
        'nor': (crear_nor, leer_nor, leer_todos_nor, actualizar_nor, borrar_nor),
        'nro': (crear_nro, leer_nro, leer_todos_nro, actualizar_nro, borrar_nro),
        'obj': (crear_obj, leer_obj, leer_todos_obj, actualizar_obj, borrar_obj),
        'org': (crear_org, leer_org, leer_todos_org, actualizar_org, borrar_org),
        'pel': (crear_pel, leer_pel, leer_todos_pel, actualizar_pel, borrar_pel),
        'per': (crear_per, leer_per, leer_todos_per, actualizar_per, borrar_per),
        'pri': (crear_pri, leer_pri, leer_todos_pri, actualizar_pri, borrar_pri),
        'projc': (crear_projc, leer_projc, leer_todos_projc, actualizar_projc, borrar_projc),
        'pro': (crear_pro, leer_pro, leer_todos_pro, actualizar_pro, borrar_pro),
        'pub': (crear_pub, leer_pub, leer_todos_pub, actualizar_pub, borrar_pub),
        'rep': (crear_rep, leer_rep, leer_todos_rep, actualizar_rep, borrar_rep),
        'res': (crear_res, leer_res, leer_todos_res, actualizar_res, borrar_res),
        'rie': (crear_rie, leer_rie, leer_todos_rie, actualizar_rie, borrar_rie),
        'ses': (crear_ses, leer_ses, leer_todos_ses, actualizar_ses, borrar_ses),
        'sugerencias': (crear_sugerencias, leer_sugerencias, leer_todos_sugerencias, actualizar_sugerencias, borrar_sugerencias),
        'tac': (crear_tac, leer_tac, leer_todos_tac, actualizar_tac, borrar_tac),
        'teccap': (crear_teccap, leer_teccap, leer_todos_teccap, actualizar_teccap, borrar_teccap),
        'tec': (crear_tec, leer_tec, leer_todos_tec, actualizar_tec, borrar_tec),
        'temjc': (crear_temjc, leer_temjc, leer_todos_temjc, actualizar_temjc, borrar_temjc),
        'tem': (crear_tem, leer_tem, leer_todos_tem, actualizar_tem, borrar_tem),
        'ten': (crear_ten, leer_ten, leer_todos_ten, actualizar_ten, borrar_ten),
        'top': (crear_top, leer_top, leer_todos_top, actualizar_top, borrar_top),
        'tpo': (crear_tpo, leer_tpo, leer_todos_tpo, actualizar_tpo, borrar_tpo),
        'val': (crear_val, leer_val, leer_todos_val, actualizar_val, borrar_val),
        'vis': (crear_vis, leer_vis, leer_todos_vis, actualizar_vis, borrar_vis)
    }

    # === CREAR ENDPOINTS DINÁMICOS ===
    for nombre, (crear, leer, leer_todos, actualizar, borrar) in servicios.items():

        # POST /modelo
        app.add_url_rule(
            f'/{nombre}',
            f'crear_{nombre}',
            lambda crear=crear: jsonify(crear(request.json)),
            methods=['POST']
        )

        # GET /modelo → leer todos
        app.add_url_rule(
            f'/{nombre}',
            f'leer_todos_{nombre}',
            lambda leer_todos=leer_todos: jsonify(leer_todos()),
            methods=['GET']
        )

        # GET /modelo/<id> → leer uno
        app.add_url_rule(
            f'/{nombre}/<idx>',
            f'leer_{nombre}',
            lambda idx, leer=leer: jsonify(leer(idx)),
            methods=['GET']
        )

        # PUT /modelo/<id>
        app.add_url_rule(
            f'/{nombre}/<idx>',
            f'actualizar_{nombre}',
            lambda idx, actualizar=actualizar: jsonify(actualizar(idx, request.json)),
            methods=['PUT']
        )

        # DELETE /modelo/<id>
        app.add_url_rule(
            f'/{nombre}/<idx>',
            f'borrar_{nombre}',
            lambda idx, borrar=borrar: jsonify(borrar(idx)),
            methods=['DELETE']
        )
