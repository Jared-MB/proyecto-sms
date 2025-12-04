<script src="../js/control.js"></script>
<?php
require_once __DIR__ . "/../core/auth/auth-service.php";
include("acceso.php");

if (isset($_POST['enviar'])) {
	$usuario = $_POST['user'];
	$pw = $_POST['pw'];

	// Use variables from acceso.php
	$ip_address = $ip ?? $_SERVER['REMOTE_ADDR'];
	$browser = $yourbrowser ?? $_SERVER['HTTP_USER_AGENT'];

	$user_data = $auth_service->login($usuario, $pw, $ip_address, $browser);

	if ($user_data) {
		$_SESSION["user"] = $user_data['id'];
		$_SESSION["nivel"] = $user_data['level'];
		$_SESSION["org"] = $user_data['organization'];
		$_SESSION["cargo"] = $user_data['position'];
		$_SESSION["nombre"] = $user_data['name'];
		$_SESSION["foto"] = $user_data['photo'];

		// Theme settings
		$_SESSION["theme"] = $user_data['theme'];
		$_SESSION["fondo"] = $user_data['background'];

		if ($_SESSION["nivel"] <= 4) {
			header("Location: ../");
		}
	} else {
		header("Location: ../index.php?USU=X");
	}
}
?>