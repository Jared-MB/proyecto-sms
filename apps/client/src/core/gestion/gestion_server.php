<?php

declare(strict_types=1);

require_once __DIR__ . '/../services/http.php';

class GestionServer
{
    private string $api_url;

    public function __construct()
    {
        $this->api_url = getenv("API_URL");
    }

    public function get_gestion_reports(): array
    {
        return Http::get($this->api_url . "/gestion/reportes");
    }
}

$gestion_server = new GestionServer();
