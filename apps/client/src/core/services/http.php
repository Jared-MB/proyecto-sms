<?php

declare(strict_types=1);

require_once __DIR__ . "/../utils/env.php";

define("API_TOKEN", getenv("API_TOKEN"));

class Http
{
    /**
     * Execute a GET request
     *
     * @param string $url
     * @param array|false $params
     * @return array
     * @throws RuntimeException
     */
    public static function get(string $url, $params = false): array
    {
        return self::request('GET', $url, $params);
    }

    /**
     * Execute a POST request
     *
     * @param string $url
     * @param mixed $data
     * @return array
     * @throws RuntimeException
     */
    public static function post(string $url, $data = false): array
    {
        return self::request('POST', $url, $data);
    }

    /**
     * Execute a PUT request
     *
     * @param string $url
     * @param mixed $data
     * @return array
     * @throws RuntimeException
     */
    public static function put(string $url, $data = false): array
    {
        return self::request('PUT', $url, $data);
    }

    /**
     * Execute a DELETE request
     *
     * @param string $url
     * @param mixed $data
     * @return array
     * @throws RuntimeException
     */
    public static function delete(string $url, $data = false): array
    {
        return self::request('DELETE', $url, $data);
    }

    /**
     * Core request handler
     *
     * @param string $method
     * @param string $url
     * @param mixed $data
     * @return array
     * @throws RuntimeException
     */
    public static function request(string $method, string $url, $data = false): array
    {
        $curl = curl_init();
        $method = strtoupper($method);

        switch ($method) {
            case "POST":
                curl_setopt($curl, CURLOPT_POST, 1);
                if ($data) {
                    // FormData handled in JS; here JSON endpoints expect json
                    // If data is array/object, strict typing might require handling,
                    // but legacy code passed $data directly for POST if it wasn't json_encoded by caller?
                    // Looking at legacy: if ($data) curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
                    // It seems legacy expected $data to be pre-formatted or an array for multipart/form-data?
                    // The comment said "FormData handled in JS; here JSON endpoints expect json"
                    // But legacy code didn't json_encode for POST, only for PUT.
                    // We will keep behavior: pass $data as is for POST.
                    curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
                }
                break;
            case "PUT":
                curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "PUT");
                if ($data) {
                    // Legacy code json_encoded $data for PUT
                    curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
                }
                break;
            case "DELETE":
                curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "DELETE");
                break;
            case "GET":
            default:
                if ($data && is_array($data)) {
                    $url = sprintf("%s?%s", $url, http_build_query($data));
                }
                break;
        }

        curl_setopt($curl, CURLOPT_URL, $url);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

        // Headers
        $headers = ["Authorization: Bearer " . API_TOKEN];

        // Add Accept header for JSON
        $headers[] = "Accept: application/json";

        // Note: Legacy code didn't explicitly set Content-Type for POST, relying on curl default or data type.
        // For PUT it sent JSON but didn't set Content-Type: application/json explicitly in headers array
        // (though it might be good practice to do so, I will stick to legacy behavior to avoid breaking things).

        curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

        $result = curl_exec($curl);

        if (curl_errno($curl)) {
            throw new \RuntimeException("Curl error: " . curl_error($curl));
        }

        $decoded = json_decode($result, true);
        if ($decoded === null && json_last_error() !== JSON_ERROR_NONE) {
            // Include raw result in exception message or handle differently?
            // Legacy returned ["error" => ..., "raw" => $result]
            // We'll throw exception with message.
            throw new \RuntimeException("Respuesta no válida del servidor");
        }

        return $decoded;
    }
}

/**
 * Legacy wrapper for backward compatibility
 * @deprecated Use Http::request() or Http::get/post/put/delete instead
 */
function callURL(string $method, string $url, $data = false)
{
    try {
        return Http::request($method, $url, $data);
    } catch (\RuntimeException $e) {
        $error = ["error" => $e->getMessage()];
        // Try to capture raw response if it was a JSON error?
        // The exception message is simple string, so we lose "raw" data if we don't pass it.
        // For now, simple error return.
        return $error;
    }
}
