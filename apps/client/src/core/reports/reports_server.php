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
}

$reports_server = new ReportsServer();
