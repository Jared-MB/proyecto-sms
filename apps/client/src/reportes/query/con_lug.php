<?php

declare(strict_types=1);

require_once __DIR__ . '/../../core/reports/reports_server.php';

try {
    $locations = $reports_server->get_locations();
    echo json_encode($locations);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
