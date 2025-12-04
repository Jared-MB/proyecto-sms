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

    public function upload_report_file(string $user, array $file): array
    {
        return Http::postMultipart($this->api_url . "/upload", [
            'evi' => $file,
            'user_id' => $user
        ]);
    }

    public function upload_report(array $data): array
    {
        return Http::post($this->api_url . "/reportes", [
            'con' => $data['confidential'],
            'fecsus' => $data['date_event'],
            'fecrep' => $data['date_report'],
            'lugsus' => $data['location'],
            'obs' => $data['observation'],
            'freeve' => $data['frequency'],
            'emp' => $data['employee'],
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

    public function update_report(string $id, array $data): array
    {
        return Http::put($this->api_url . "/rep/" . $id, [
            'CONREP' => $data['confidential'],
            'FECEVE' => $data['date_event'],
            'FECREP' => $data['date_report'],
            'LUGREP' => $data['location'],
            'OBSREP' => $data['observation'],
            'FREREP' => $data['frequency'],
            'PERREP' => $data['employee'],
            'CANREP' => $data['cancelled']
        ]);
    }

    public function delete_report(string $id): array
    {
        return Http::delete($this->api_url . "/rep/" . $id);
    }

    public function get_locations(): array
    {
        return Http::get($this->api_url . "/lugares");
    }

    public function get_areas(): array
    {
        return Http::get($this->api_url . "/coordinaciones");
    }

    public function get_employees(string $area_id): array
    {
        return Http::get($this->api_url . "/empleados", ['area' => $area_id]);
    }
}

$reports_server = new ReportsServer();
