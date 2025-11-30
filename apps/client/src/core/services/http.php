<?php

require_once __DIR__ . "/../utils/env.php";

define("API_TOKEN", getenv("API_TOKEN"));

function http_request(string $method, string $url, $data = false)
{
    $curl = curl_init();
    switch (strtoupper($method)) {
        case "POST":
            curl_setopt($curl, CURLOPT_POST, 1);
            if ($data) curl_setopt($curl, CURLOPT_POSTFIELDS, $data); // FormData handled in JS; here JSON endpoints expect json
            break;
        case "PUT":
            curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "PUT");
            if ($data) curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
            break;
        case "DELETE":
            curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "DELETE");
            break;
        case "GET":
        default:
            if ($data && is_array($data)) {
                $url = sprintf("%s?%s", $url, http_build_query($data));
            }
    }

    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

    // Headers: si envías JSON usa Content-Type, si esperas FormData en POST no agregues Content-Type
    $headers = ["Authorization: Bearer " . API_TOKEN];
    // Si estás solicitando JSON (GET) indicarlo
    $headers[] = "Accept: application/json";

    curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
    $result = curl_exec($curl);

    if (curl_errno($curl)) {
        $err = curl_error($curl);
        return ["error" => "Curl error: " . $err];
    }

    $decoded = json_decode($result, true);
    if ($decoded === null && json_last_error() !== JSON_ERROR_NONE) {
        // Respuesta no JSON o vacía
        return ["error" => "Respuesta no válida del servidor", "raw" => $result];
    }

    return $decoded;
}
