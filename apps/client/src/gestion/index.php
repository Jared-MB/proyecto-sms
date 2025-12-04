<?php
session_start();

require_once __DIR__ . "/../core/gestion/gestion_server.php";
require_once __DIR__ . "/../core/auth/logout.php";

if (!isset($_SESSION["user"]) || !isset($_SESSION["nivel"]) || $_SESSION["nivel"] > 2) {
    logout('../');
}

$user = $_SESSION['user'];
$reportes = $gestion_server->get_gestion_reports();

?>
<html>

<head>
    <script src="../js/jquery-3.3.1.min.js"></script>
    <script src="../js/control.js"></script>
    <script type="text/javascript" language="javascript" src="../TableFilter-master/dist/tablefilter/tablefilter.js"></script>
    <?php
    require_once("head.html");
    $theme = $_SESSION['theme'] ?? 1;
    if ($theme == 1) {
        include("menu_index.html");
    } else {
        include("menus_2/menu_index.html");
    }
    ?>
</head>

<body style="background-color:#eee;">
    <div class="ventana_3">
        <?php include("ventanas_modales/e_ges.html"); ?>
    </div>

    <div style="height:92%;overflow-y: scroll;">
        <div class="reporte">
            <?php if (empty($reportes)) { ?>
                <br>
                <h2 align="center">NO HAY REPORTES EN GESTIÓN </h2>
            <?php } else { ?>
                <div class="tabla reportes">
                    <table id="tabla_ges">
                        <thead>
                            <tr>
                                <th rowspan="2">MES</th>
                                <th width="20px" rowspan="2">N°</th>
                                <th rowspan="2">FECHA DE REPORTE</th>
                                <th rowspan="2">FECHA INICIO GESTIÓN</th>
                                <th rowspan="2">QUIEN GESTIONA</th>
                                <th colspan="3" bgcolor="red">PELIGRO</th>
                                <th rowspan="2">CATEGORÍA DEL PELIGRO</th>
                                <th bgcolor="green" colspan="1">A</th>
                                <th rowspan="2">MÉTODO DE IDENTIFICACIÓN DEL PELIGRO</th>
                                <th rowspan="2">ESTATUS</th>
                                <th rowspan="2">VER GESTIÓN</th>
                                <th rowspan="2"></th>
                            </tr>
                            <tr>
                                <th style="color:#fff000">CONDICIÓN</th>
                                <th style="color:#fff000">OBJETO</th>
                                <th style="color:#fff000">ACTIVIDAD</th>
                                <th bgcolor="#ccc" style="color:#000">PELIGRO GENÉRICO</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php
                            // Asegurarnos de que locale esté configurado
                            setlocale(LC_TIME, 'es_MX.UTF-8', 'es_MX', 'es_ES.UTF-8', 'spanish');

                            foreach ($reportes as $row) {
                                $iderep = $row['IDEREP'];
                                $fecrep = $row['FECREP'] ? date("d-m-Y", strtotime($row['FECREP'])) : '';
                                $fecpel = $row['FECPEL'] ? date("d-m-Y", strtotime($row['FECPEL'])) : '';

                                $mes = '';
                                if ($row['FECREP']) {
                                    $mes = mb_strtoupper(date("M", strtotime($row['FECREP'])));
                                }
                            ?>
                                <tr>
                                    <td style="color:#fff; background-color:#2672EC"><?php echo htmlspecialchars($mes); ?></td>
                                    <td align="center"><?php echo htmlspecialchars((string)$iderep); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($fecrep); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($fecpel); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($row['NOMGESPEL']); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($row['CONPEL']); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($row['OBJPEL']); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($row['ACTPEL']); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($row['CATEPEL']); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($row['GENPEL']); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($row['METIDEPEL']); ?></td>
                                    <td align="center"><?php echo htmlspecialchars($row['ESTMON']); ?></td>
                                    <td align="center">
                                        <a href="ver_gestion.php?IDEREP=<?php echo $iderep; ?>">
                                            <img height="20px" src="../imagenes/gestion.png" alt="Ver Gestión">
                                        </a>
                                    </td>
                                    <td>
                                        <?php if ($_SESSION["nivel"] != 2) { ?>
                                            <a href="javascript:openventana_var('.ventana_3',<?php echo $iderep; ?>,'IDREP','g3');">
                                                <img height='20px' src='../imagenes/edit.png' alt="Editar">
                                            </a>
                                        <?php } ?>
                                    </td>
                                </tr>
                            <?php } ?>
                        </tbody>
                    </table>
                </div>
            <?php } ?>
        </div>
    </div>
</body>
<script type="text/javascript">
    filtro_ges();
</script>

</html>