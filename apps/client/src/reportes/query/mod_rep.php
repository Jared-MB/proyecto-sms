<?php

declare(strict_types=1);

require_once __DIR__ . '/../../core/reports/reports_server.php';

$id = $_POST['IDREP'] ?? '';

try {
	if (isset($_POST['eliminar'])) {
		$reports_server->delete_report($id);
		echo "Reporte eliminado";
	} else {
		$data = [
			'confidential' => $_POST["con_e"] ?? 0,
			'date_event' => $_POST["fecsus_e"] ?? '',
			'date_report' => $_POST["fecrep_e"] ?? '',
			'location' => $_POST["lugsus_e"] ?? '',
			'observation' => mb_strtoupper($_POST["obs_e"] ?? ''),
			'frequency' => $_POST["freeve_e"] ?? '',
			'employee' => $_POST["emp_e"] ?? '',
			'cancelled' => $_POST["canrep_e"] ?? 0
		];
		$reports_server->update_report($id, $data);
	}
	header("Location:../index.php");
} catch (Exception $e) {
	die($e->getMessage());
}
