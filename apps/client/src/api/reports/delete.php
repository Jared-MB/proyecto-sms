<?php

declare(strict_types=1);

require_once __DIR__ . '/../../core/reports/reports_server.php';
require_once __DIR__ . '/../../core/auth/auth-service.php';

session_start();

if ($_SERVER['REQUEST_METHOD'] !== 'DELETE') {
    http_response_code(405);
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

try {
    $response = $reports_server->delete_report($id);
    header('Content-Type: application/json');
    echo json_encode($response);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
