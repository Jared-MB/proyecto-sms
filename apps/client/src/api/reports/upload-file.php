<?php

declare(strict_types=1);

require_once __DIR__ . '/../../core/reports/reports_server.php';
require_once __DIR__ . '/../../core/auth/auth-service.php';

session_start();

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(404);
    exit;
}


if (!isset($_SESSION["user"]) || !isset($_SESSION["nivel"]) || $_SESSION["nivel"] > 2) {
    $auth_service->logout('../../');
}

$errors = [];

if (!ini_get('file_uploads')) {
    $errors[] = "File uploads are DISABLED in php.ini (file_uploads = Off)";
}
$tmpDir = ini_get('upload_tmp_dir') ?: sys_get_temp_dir();
if (!is_dir($tmpDir)) {
    $errors[] = "Temp directory does not exist: $tmpDir";
} elseif (!is_writable($tmpDir)) {
    $errors[] = "Temp directory is not writable: $tmpDir";
}

// If there are critical errors, report them
if (!empty($errors)) {
    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'Upload configuration issues detected',
        'issues' => $errors,
        'files_received' => !empty($_FILES),
        'post_received' => !empty($_POST)
    ]);
    exit;
}

// Check if file was received
if (empty($_FILES['evi'])) {
    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'No file received',
        'debug' => [
            'files_array' => $_FILES,
            'post_array' => $_POST,
            'content_type' => $_SERVER['CONTENT_TYPE'] ?? 'not set',
            'content_length' => $_SERVER['CONTENT_LENGTH'] ?? 'not set'
        ]
    ]);
    exit;
}

// Check for upload errors
if ($_FILES['evi']['error'] !== UPLOAD_ERR_OK) {
    $errorMessages = [
        UPLOAD_ERR_INI_SIZE => 'File exceeds upload_max_filesize (' . ini_get('upload_max_filesize') . ')',
        UPLOAD_ERR_FORM_SIZE => 'File exceeds MAX_FILE_SIZE from HTML form',
        UPLOAD_ERR_PARTIAL => 'File was only partially uploaded',
        UPLOAD_ERR_NO_FILE => 'No file was uploaded',
        UPLOAD_ERR_NO_TMP_DIR => 'Missing temporary folder',
        UPLOAD_ERR_CANT_WRITE => 'Failed to write file to disk',
        UPLOAD_ERR_EXTENSION => 'A PHP extension stopped the file upload'
    ];

    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'Upload failed',
        'message' => $errorMessages[$_FILES['evi']['error']] ?? 'Unknown error',
        'error_code' => $_FILES['evi']['error']
    ]);
    exit;
}


try {
    $response = $reports_server->upload_report_file($_SESSION['user'], $_FILES['evi']);
    header('Content-Type: application/json');
    echo json_encode($response);
} catch (Exception $e) {
    header('Content-Type: application/json');
    http_response_code(500);
    echo json_encode([
        'error' => 'Failed to upload to server',
        'message' => $e->getMessage()
    ]);
}
exit;
