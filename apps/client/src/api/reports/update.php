<?php

declare(strict_types=1);

require_once __DIR__ . '/../../core/reports/reports_server.php';
require_once __DIR__ . '/../../core/auth/auth-service.php';

session_start();

if ($_SERVER['REQUEST_METHOD'] !== 'PUT') {
    http_response_code(405); // Method Not Allowed
    exit;
}

if (!isset($_SESSION["user"]) || !isset($_SESSION["nivel"]) || $_SESSION["nivel"] > 2) {
    $auth_service->logout('../../');
}

$id = $_GET['id'] ?? '';

if (!$id) {
    http_response_code(400);
    echo json_encode(['error' => 'Missing ID']);
    exit;
}

$input = json_decode(file_get_contents('php://input'), true);

try {
    $data = [
        'confidential' => $input['CONREP'] ?? 0,
        'date_event' => $input['FECEVE'] ?? '',
        'date_report' => $input['FECREP'] ?? '',
        'location' => $input['LUGREP'] ?? '',
        'observation' => $input['OBSREP'] ?? '',
        'frequency' => $input['FREREP'] ?? '',
        'employee' => $input['PERREP'] ?? '',
        'cancelled' => $input['CANREP'] ?? 0
    ];
    $response = $reports_server->update_report($id, $data);
    header('Content-Type: application/json');
    echo json_encode($response);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
