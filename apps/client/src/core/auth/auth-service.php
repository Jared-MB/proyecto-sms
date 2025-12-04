<?php

declare(strict_types=1);

require_once __DIR__ . '/../services/database.php';

class AuthService
{
    private $db;

    public function __construct()
    {
        $this->db = Database::getInstance()->connect();
    }

    public function login(string $username, string $password, string $ip, string $browser_info): ?array
    {
        try {
            // Query to find user
            $sql = "SELECT p.IDEPER, e.NOMEMP, e.APPEMP, e.APMEMP, s.PRISES, e.FOTEMP, c.NOMCAR, c.ORGCAR 
                    FROM EMP e
                    JOIN PER p ON e.IDEEMP = p.EMPPER
                    JOIN CAR c ON p.CARPER = c.IDECAR
                    JOIN SES s ON p.IDEPER = s.IDESES
                    WHERE e.EMAEMP = :username AND s.PASSES = :password";

            $stmt = $this->db->prepare($sql);
            $stmt->bindParam(':username', $username);
            $stmt->bindParam(':password', $password);
            $stmt->execute();

            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($user) {
                // Log access
                $this->logAccess($ip, $browser_info, (int)$user['IDEPER']);

                // Get theme
                $themeData = $this->getTheme((int)$user['IDEPER']);

                return [
                    'id' => $user['IDEPER'],
                    'name' => $user['NOMEMP'] . ' ' . $user['APPEMP'] . ' ' . $user['APMEMP'],
                    'level' => $user['PRISES'],
                    'position' => $user['NOMCAR'],
                    'organization' => $user['ORGCAR'],
                    'photo' => $user['FOTEMP'],
                    'theme' => $themeData['theme'],
                    'background' => $themeData['background']
                ];
            }

            return null;
        } catch (PDOException $e) {
            // Log error if needed
            error_log("Login error: " . $e->getMessage());
            return null;
        }
    }

    private function logAccess(string $ip, string $browser_info, int $userId): void
    {
        try {
            $sql = "INSERT INTO ACCESOS (DIRACC, FECACC, BROACC, USEACC) VALUES (:ip, NOW(), :browser, :user)";
            $stmt = $this->db->prepare($sql);
            $stmt->bindParam(':ip', $ip);
            $stmt->bindParam(':browser', $browser_info);
            $stmt->bindParam(':user', $userId);
            $stmt->execute();
        } catch (PDOException $e) {
            error_log("Access log error: " . $e->getMessage());
        }
    }

    private function getTheme(int $userId): array
    {
        try {
            $sql = "SELECT tip_asp, img_asp FROM asp WHERE ide_usu = :user";
            $stmt = $this->db->prepare($sql);
            $stmt->bindParam(':user', $userId);
            $stmt->execute();

            $result = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($result) {
                return [
                    'theme' => $result['tip_asp'],
                    'background' => $result['img_asp']
                ];
            }
        } catch (PDOException $e) {
            error_log("Theme fetch error: " . $e->getMessage());
        }

        return [
            'theme' => 1,
            'background' => 'img/fondo.jpg'
        ];
    }
    public function logout(string $to = "../"): void
    {
        if (session_status() === PHP_SESSION_NONE) {
            session_start();
        }

        $_SESSION = array();

        if (ini_get("session.use_cookies")) {
            $params = session_get_cookie_params();
            setcookie(
                session_name(),
                '',
                time() - 42000,
                $params["path"],
                $params["domain"],
                $params["secure"],
                $params["httponly"]
            );
        }

        session_destroy();

        header("Location: " . $to);
        exit();
    }
}

$auth_service = new AuthService();
