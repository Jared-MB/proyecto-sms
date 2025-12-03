<?php

declare(strict_types=1);

require_once __DIR__ . '/../services/http.php';

class ReportsServer
{

    private string $api_url;

    public function __construct()
    {
        $this->api_url = getenv("API_URL");
    }

    public function get_reports_by_user(string $user): array
    {
        return Http::get($this->api_url . "/reportes-completo/$user");
    }

    public function get_files_by_user(string $user): array
    {
        return Http::get($this->api_url . "/list/$user");
    }

    public function upload_report(string $user, array $file): array
    {
        return Http::postMultipart($this->api_url . "/upload", [
            'evi' => $file,
            'user_id' => $user
        ]);
    }

    public function delete_file(string $user, string $filename): array
    {
        try {
            $result = Http::delete($this->api_url . "/file/$user/$filename");
            return ['success' => true, 'message' => $result['message'] ?? 'Archivo eliminado'];
        } catch (\RuntimeException $e) {
            return ['success' => false, 'error' => $e->getMessage()];
        }
    }
}

$reports_server = new ReportsServer();
