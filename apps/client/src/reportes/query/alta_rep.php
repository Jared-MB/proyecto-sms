<?php

declare(strict_types=1);

require_once __DIR__ . '/../../core/reports/reports_server.php';

$data = [
    'confidential' => $_POST["con"] ?? 0,
    'date_event' => $_POST["fecsus"] ?? '',
    'date_report' => $_POST["fecrep"] ?? '',
    'location' => $_POST["lugsus"] ?? '',
    'observation' => mb_strtoupper($_POST["obs"] ?? ''),
    'frequency' => $_POST["freeve"] ?? '',
    'employee' => $_POST["emp"] ?? ''
];

try {
    $reports_server->upload_report($data);
} catch (Exception $e) {
    die($e->getMessage());
}
