<?php

declare(strict_types=1);

require_once __DIR__ . "/../utils/env.php";

class Database
{
    private static $instance = null;
    private $pdo = null;

    private $host;
    private $db_name;
    private $user;
    private $password;

    // Private constructor prevents direct instantiation
    private function __construct()
    {
        $this->host = getenv("DB_HOST");
        $this->db_name = getenv("DB_NAME");
        $this->user = getenv("DB_USER");
        $this->password = getenv("DB_PASSWORD");
    }

    // Get the single instance
    public static function getInstance(): self
    {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    public function connect(): PDO
    {
        if ($this->pdo === null) {
            try {
                $this->pdo = new PDO("mysql:host=" . $this->host . ";dbname=" . $this->db_name, $this->user, $this->password);
                $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            } catch (PDOException $e) {
                throw new \Exception("Connection failed: " . $e->getMessage());
            }
        }
        return $this->pdo;
    }
}

$db = Database::getInstance()->connect();
