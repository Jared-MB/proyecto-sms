<?php

declare(strict_types=1);

require_once __DIR__ . '/../../core/reports/reports_server.php';
require_once __DIR__ . '/../../core/auth/logout.php';

session_start();

if (!isset($_SESSION['user'])) {
    logout('../../');
}

if (!isset($_FILES['evi'])) {
    die("Error: No file uploaded.");
}

try {
    $reports_server->upload_report_file($_SESSION['user'], $_FILES['evi']);

    $iderep = $_POST['IDEREP'] ?? '';
    header("Location: ../evidencias.php?IDEREP=$iderep");
} catch (Exception $e) {
    die($e->getMessage());
}
