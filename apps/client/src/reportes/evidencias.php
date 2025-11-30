<?php
session_start();
if (isset($_SESSION["user"])) {
  if ($_SESSION["nivel"] <= 2) {
    $user = $_SESSION['user'];
    $iderep = $_GET['IDEREP'];
    $api_token = "MI_TOKEN_SEGURO_12345";
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
      $theme = $_SESSION['theme'] ?? 0;
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

          <?php
          // --- Obtener archivos del microservicio Flask ---
          $ch = curl_init();
          curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:5001/list/$user");
          curl_setopt($ch, CURLOPT_HTTPHEADER, ["Authorization: Bearer $api_token"]);
          curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
          $response = curl_exec($ch);
          curl_close($ch);
          $archivos = json_decode($response, true);

          if (empty($archivos)) {
            echo "<h3>No existen scans</h3><br>";
          } else {
            foreach ($archivos as $file) {
              $url = "http://127.0.0.1:5001/file/$user/$file";
              $es_pdf = str_ends_with($file, ".pdf");
              echo '<div class="image_wrapper">';
              echo '<a href="' . $url . '" target="_blank">';
              if ($es_pdf) echo '<img src="../imagenes/icono_pdf.png" width="150" height="150">';
              else echo '<img src="' . $url . '" width="100" height="100">';
              echo '</a>';
              echo '<a href="#" onclick="eliminarArchivo(\'' . $file . '\')">';
              echo '<img src="../imagenes/eliminar_cuadro.jpg" title="Eliminar" class="remove"></a>';
              echo '</div>';
            }
          }
          ?>

          <!-- Formulario de subida -->
          <form method="post" id="form" enctype="multipart/form-data">
            <table>
              <input type="hidden" id="IDEREP" name="IDEREP" value="<?php echo $iderep; ?>">
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

          <form method="post" id="form_adicional" enctype="multipart/form-data">
            <table>
              <input type="hidden" id="IDEREP" name="IDEREP" value="<?php echo $iderep; ?>">
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

      <script>
        // Subida archivo principal
        $('#form').on('submit', function(e) {
          e.preventDefault();
          const formData = new FormData(this);
          formData.append('user_id', '<?php echo $user; ?>');
          fetch('http://127.0.0.1:5001/upload', {
              method: 'POST',
              headers: {
                'Authorization': 'Bearer <?php echo $api_token; ?>'
              },
              body: formData
            })
            .then(res => res.json())
            .then(data => {
              alert(data.message || JSON.stringify(data));
              location.reload();
            })
            .catch(err => alert("Error al conectar con el servicio: " + err));
        });

        // Subida archivo adicional
        $('#form_adicional').on('submit', function(e) {
          e.preventDefault();
          const formData = new FormData(this);
          formData.append('user_id', '<?php echo $user; ?>');
          fetch('http://127.0.0.1:5001/upload', {
              method: 'POST',
              headers: {
                'Authorization': 'Bearer <?php echo $api_token; ?>'
              },
              body: formData
            })
            .then(res => res.json())
            .then(data => {
              alert(data.message || JSON.stringify(data));
              location.reload();
            })
            .catch(err => alert("Error al conectar con el servicio: " + err));
        });

        // Eliminar archivo
        function eliminarArchivo(nombreArchivo) {
          const user_id = '<?php echo $user; ?>';
          if (!confirm("¿Seguro que quieres eliminar este archivo?")) return;
          fetch(`http://127.0.0.1:5001/file/${user_id}/${nombreArchivo}`, {
              method: 'DELETE',
              headers: {
                'Authorization': 'Bearer <?php echo $api_token; ?>'
              }
            })
            .then(r => r.json())
            .then(data => {
              alert(data.message || data.error);
              location.reload();
            })
            .catch(err => alert("Error al eliminar: " + err));
        }
      </script>

    </body>

    </html>
<?php
  } else {
    session_destroy();
    header("Location: ../");
  }
} else {
  header("Location: ../");
}
?>