<?php

declare(strict_types=1);

require_once __DIR__ . '/../core/reports/reports_server.php';
require_once __DIR__ . '/../core/auth/logout.php';

session_start();

if (!isset($_SESSION["user"]) || !isset($_SESSION["nivel"]) || $_SESSION["nivel"] > 2) {
    logout();
}

$user = $_SESSION['user'];
$report_id = $_GET['IDEREP'];
$apiHost = getenv('API_URL');
$files = $reports_server->get_files_by_user($user);

?>
<!DOCTYPE html>
<html>

<head>
    <?php include("header.html"); ?>
    <script src="../js/jquery-3.3.1.min.js"></script>
    <script src="../js/control.js"></script>
    <script src="js/jquery.validate.min.js"></script>
    <script src="js/validar_rep.js"></script>
    <script src="js/validar_lug.js"></script>
    <script type="text/javascript" src="../TableFilter-master/dist/tablefilter/tablefilter.js"></script>
</head>

<body style="background-color:#eee;">

    <?php
    $theme = $_SESSION['theme'] ?? 1;
    if ($theme == 1) include("menu_evi.html");
    else include("menu_evi_2.html");

    include("ventanas_modales/b_evi.html");
    include("ventanas_modales/e_rep.html");
    include("ventanas_modales/n_lugar.html");
    ?>

    <div style="height:92%;overflow-y: scroll; margin:1em;margin-left:2.5em;">
        <div class="f2">
            <h1>Reporte (Escaneo del reporte físico)</h1>
            <br>

            <?php if (empty($files)): ?>

                <h3>No existen scans</h3><br>

            <?php else: ?>

                <div>
                    <?php foreach ($files as $file): ?>
                        <?php
                        $safeFile = htmlspecialchars($file, ENT_QUOTES, 'UTF-8');
                        $fileUrl  = "{$apiHost}/file/{$user}/{$safeFile}";
                        $isPdf    = str_ends_with($file, ".pdf");

                        if ($isPdf) {
                            $thumbSrc = "../imagenes/icono_pdf.png";
                            $size = 'width="150" height="150"';
                        } else {
                            $thumbSrc = $fileUrl;
                            $size = 'width="100" height="100"';
                        }
                        ?>

                        <div class="image_wrapper">
                            <a href="<?= $fileUrl ?>" target="_blank">
                                <img src="<?= $thumbSrc ?>" <?= $size ?> alt="File Preview">
                            </a>

                            <button type='button' class='remove' data-file="<?= $safeFile ?>">
                                X
                            </button>
                        </div>

                    <?php endforeach; ?>
                </div>

            <?php endif; ?>

            <!-- Formulario de subida -->
            <form id="form" class='file-form' enctype="multipart/form-data">
                <table>
                    <input type="hidden" id="IDEREP" name="IDEREP" value="<?php echo $report_id; ?>">
                    <input type="hidden" id="tip" name="tip" value="FISICA">
                    <input type="hidden" id="nom" name="nom" value="REPORTE">
                    <tr>
                        <td><input type="file" id="evi" name="evi" accept="application/pdf"></td>
                    </tr>
                    <tr>
                        <td>
                            <div class="buttons">
                                <input type="submit" class="boton" value="Subir" name="enviar" id="enviar">
                            </div>
                        </td>
                    </tr>
                </table>
            </form>

            <div style="margin-top:1em;">
                <b>Nota:</b> Tamaño máximo por archivo 10MB, solo PDF.
            </div>
        </div>

        <!-- SECCIÓN DE EVIDENCIAS ADICIONALES -->
        <div class="f2">
            <br><br>
            <h1>Evidencias adicionales</h1>
            <br>

            <!-- Listado dinámico usando Flask -->
            <div id="evia_list"></div>

            <form id="form_adicional" class='file-form' enctype="multipart/form-data">
                <table>
                    <input type="hidden" id="IDEREP" name="IDEREP" value="<?php echo $report_id; ?>">
                    <input type="hidden" id="nom" name="nom" value="ADICIONAL">
                    <tr>
                        <td><b>Tipo de evidencia: </b>
                            <select id="tip" name="tip" style="width:100px">
                                <option selected>--ELEGIR--</option>
                                <option value="FISICA">FISICA</option>
                                <option value="TESTIMONIAL">TESTIMONIAL</option>
                                <option value="DOCUMENTAL">DOCUMENTAL</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td><input type="file" id="evi" name="evi" accept="application/pdf, .jpg, .png"></td>
                    </tr>
                    <tr>
                        <td>
                            <div class="buttons">
                                <input type="submit" class="boton" value="Subir" name="enviar" id="enviar_adicional">
                            </div>
                        </td>
                    </tr>
                </table>
            </form>
            <div style="margin-top:1em;">
                <b>Nota:</b> Tamaño máximo por archivo 10MB
            </div>
        </div>
    </div>

    <script type='module'>
        const $forms = document.querySelectorAll('.file-form');

        $forms?.forEach($form => {
            $form.addEventListener('submit', async (e) => {
                e.preventDefault();

                const formData = new FormData(e.target);

                const response = await fetch('/api/reports/upload.php', {
                    method: 'POST',
                    body: formData,
                });

                const data = await response.json();
                alert(data.message || JSON.stringify(data));
                location.reload();
            });
        });

        const $files = document.querySelectorAll('.remove');

        $files?.forEach($file => {
            $file.addEventListener('click', async (e) => {
                e.preventDefault();

                const filename = e.target.dataset.file;

                if (!confirm(`¿Seguro que quieres eliminar este archivo? ${filename}`)) return;

                const payload = new FormData()
                payload.append('filename', filename)

                const response = await fetch('/api/reports/delete.php', {
                    method: 'POST',
                    body: payload,
                });

                const data = await response.json();
                alert(data.message || JSON.stringify(data));
                location.reload();
            });
        });
    </script>

</body>

</html>