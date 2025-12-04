<?php

declare(strict_types=1);

require_once __DIR__ . '/../../core/reports/reports_server.php';
require_once __DIR__ . '/../../core/auth/logout.php';

session_start();

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(404);
    exit;
}

if (!isset($_SESSION["user"]) || !isset($_SESSION["nivel"]) || $_SESSION["nivel"] > 2) {
    logout('../../');
}

try {
    $response = $reports_server->upload_report($_POST);
    header('Content-Type: application/json');
    echo json_encode($response);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
