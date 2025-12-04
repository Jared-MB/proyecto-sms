<?php

declare(strict_types=1);

require_once __DIR__ . '/../../core/reports/reports_server.php';

try {
    $area_id = $_GET['IDECOO'] ?? '';
    $employees = $reports_server->get_employees($area_id);
    echo json_encode($employees);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
