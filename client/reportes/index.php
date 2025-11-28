<?php
session_start();

if (!isset($_SESSION["user"])) {
    header("Location: ../");
    exit;
}
if (!isset($_SESSION["nivel"]) || $_SESSION["nivel"] > 2) {
    session_destroy();
    header("Location: ../");
    exit;
}

$user = $_SESSION['user'];

// URL base de tu API Flask
$API_URL = "http://127.0.0.1:5001";
define("API_TOKEN", "MI_TOKEN_SEGURO_12345");

function callAPI($method, $url, $data = false) {
    $curl = curl_init();
    switch (strtoupper($method)) {
        case "POST":
            curl_setopt($curl, CURLOPT_POST, 1);
            if ($data) curl_setopt($curl, CURLOPT_POSTFIELDS, $data); // FormData handled in JS; here JSON endpoints expect json
            break;
        case "PUT":
            curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "PUT");
            if ($data) curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
            break;
        case "DELETE":
            curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "DELETE");
            break;
        case "GET":
        default:
            if ($data && is_array($data)) {
                $url = sprintf("%s?%s", $url, http_build_query($data));
            }
    }

    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

    // Headers: si envías JSON usa Content-Type, si esperas FormData en POST no agregues Content-Type
    $headers = ["Authorization: Bearer " . API_TOKEN];
    // Si estás solicitando JSON (GET) indicarlo
    $headers[] = "Accept: application/json";

    curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
    $result = curl_exec($curl);

    if (curl_errno($curl)) {
        $err = curl_error($curl);
        curl_close($curl);
        return ["error" => "Curl error: " . $err];
    }

    curl_close($curl);
    $decoded = json_decode($result, true);
    if ($decoded === null && json_last_error() !== JSON_ERROR_NONE) {
        // Respuesta no JSON o vacía
        return ["error" => "Respuesta no válida del servidor", "raw" => $result];
    }
    return $decoded;
}

// ============================================================
// OBTENER TODOS LOS REPORTES (desde la API)
// ============================================================
$reportes = callAPI("GET", "$API_URL/reportes-completo/$user");

// Si la API devolvió error, podemos mostrar mensaje y usar arreglo vacío
if (isset($reportes["error"])) {
    $api_error = $reportes["error"] . (isset($reportes["raw"]) ? " | Raw: " . substr($reportes["raw"], 0, 300) : "");
    $reportes = [];
} elseif (!is_array($reportes)) {
    $reportes = [];
}

?>
<!DOCTYPE html>
<html>
<head>
    <?php include("header.html"); ?>
    <script src="../TableFilter-master/dist/tablefilter/tablefilter.js"></script>
    <script src="../js/jquery-3.3.1.min.js"></script>
    <script src="../js/control.js"></script>
    <script src="js/jquery.validate.min.js"></script>
    <script src="js/validar_rep.js"></script>
    <script src="js/validar_lug.js"></script>
    <meta charset="utf-8">
    <title>Reportes</title>
</head>
<body style="background-color:#eee;">
<?php
$theme = $_SESSION['theme'] ?? 0;
if ($theme == 1) {
    if ($_SESSION["nivel"] == 2) include("menus_directivo/menu_rep.html");
    else include("menu_rep.html");
} else {
    include("menu_rep_2.html");
}

include("ventanas_modales/n_rep.html");
include("ventanas_modales/e_rep.html");
include("ventanas_modales/n_lugar.html");
include("ventanas_modales/ayuda.html");
?>

<div class="reporte">
    <?php
    if (!empty($api_error)) {
        echo "<div style='color:darkred; margin:1em 0;'><strong>Error al consultar la API:</strong> " . htmlspecialchars($api_error) . "</div>";
    }
    ?>

    <?php if (!is_array($reportes) || count($reportes) == 0) { ?>
        <br><h2 align="center">No hay nuevos reportes por gestionar</h2>
    <?php } else { ?>

    <div class="tabla reportes">
        <div style="height:92%;overflow-y:scroll;">
            <table id="tabla_rep">
                <thead>
                    <tr>
                        <th>MES</th>
                        <th>N°</th>
                        <th>FECHA DEL REPORTE</th>
                        <th>FECHA DEL SUCESO</th>
                        <th>LUGAR DEL SUCESO</th>
                        <th>FRECUENCIA</th>
                        <th>OBSERVACIONES</th>
                        <th>REPORTANTE</th>
                        <?php if ($_SESSION["nivel"] < 2) { ?>
                            <th>EVIDENCIA</th>
                            <th>EDITAR</th>
                            <th>GESTIÓN</th>
                        <?php } ?>
                    </tr>
                </thead>
                <tbody>
                <?php
                // Asegurarnos de que locale esté configurado (para obtener meses en español)
                setlocale(LC_TIME, 'es_MX.UTF-8', 'es_MX', 'es_ES.UTF-8', 'spanish');

                foreach ($reportes as $row) {
                    // Uso de null coalescing para evitar undefined index
                    $id = $row['IDEREP'] ?? '';
                    $fec_rep_raw = $row['FECREP'] ?? '';
                    $fec_eve_raw = $row['FECEVE'] ?? '';
                    $fre = $row['FREREP'] ?? '';
                    $obs = $row['OBSREP'] ?? '';
                    $nomlug = $row['NOMLUG'] ?? '';
                    $canrep = isset($row['CANREP']) ? (int)$row['CANREP'] : 0;

                    // Formateo de fechas: solo si vienen
                    $fecrep = $fec_rep_raw ? date("d-m-Y", strtotime($fec_rep_raw)) : '';
                    $feceve = $fec_eve_raw ? date("d-m-Y", strtotime($fec_eve_raw)) : '';

                    // Mes en mayúsculas (si tenemos fecha de reporte)
                    if ($fec_rep_raw && strtotime($fec_rep_raw) !== false) {
                        $mes = mb_strtoupper(strftime("%B", strtotime($fec_rep_raw)));
                    } else {
                        $mes = '';
                    }

                    // Composición segura del nombre del reportante (evitamos warnings)
                    $nomemp = $row['NOMEMP'] ?? '';
                    $appe = $row['APPEMP'] ?? '';
                    $apme = $row['APMEMP'] ?? '';
                    $reportante = trim("$nomemp $appe $apme");

                    // Escapar contenido para evitar XSS
                    $mes_html = htmlspecialchars($mes);
                    $id_html = htmlspecialchars($id);
                    $fecrep_html = htmlspecialchars($fecrep);
                    $feceve_html = htmlspecialchars($feceve);
                    $nomlug_html = htmlspecialchars($nomlug);
                    $fre_html = htmlspecialchars($fre);
                    $obs_html = htmlspecialchars($obs);
                    $reportante_html = htmlspecialchars(mb_strtoupper($reportante));

                    // Estilo si cancelado
                    $row_style = $canrep === 1 ? 'style="color:red;"' : '';
                ?>
                    <tr <?php echo $row_style; ?>>
                        <td style="color:#fff; background-color:#2672EC;"><?php echo $mes_html; ?></td>
                        <td align="center"><?php echo $id_html; ?></td>
                        <td align="center"><?php echo $fecrep_html; ?></td>
                        <td align="center"><?php echo $feceve_html; ?></td>
                        <td align="center"><?php echo $nomlug_html; ?></td>
                        <td align="center"><?php echo $fre_html; ?></td>
                        <td align="center"><?php echo $obs_html; ?></td>
                        <td align="center"><?php echo $reportante_html; ?></td>

                        <?php if ($_SESSION["nivel"] < 2) { ?>
                            <td align="center">
                                <a href="evidencias.php?IDEREP=<?php echo urlencode($id); ?>">
                                    <img height="20px" src="../imagenes/evidencia.png" alt="Evidencias">
                                </a>
                            </td>
                            <td align="center">
                                <a href="javascript:openventana_var('.ventana_2',<?php echo $id_html; ?>,'IDREP',1);">
                                    <img height="20px" src="../imagenes/edit.png" alt="Editar">
                                </a>
                            </td>
                            <td align="center">
                                <a href="../gestion/ver_gestion.php?IDEREP=<?php echo urlencode($id); ?>">
                                    <img height="20px" src="../imagenes/sin_gestion.png" alt="Gestión">
                                </a>
                            </td>
                        <?php } ?>
                    </tr>
                <?php } // foreach ?>
                </tbody>
            </table>
        </div>
    </div>

    <?php } // else hay reportes ?>
</div>

<script>
    // Mantengo tus funciones JS tal cual (recomendación: mover a archivo .js si no está)
    cargar_coo("area");
    cargar_lug();
    cargar_fac();
    filtro_rep();
</script>
</body>
</html>
