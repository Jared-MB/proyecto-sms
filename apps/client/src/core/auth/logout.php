<?php

/**
 * Cierra la sesión y redirige al usuario a la página de inicio.
 *
 * @param string $to URL a la que se redirige al usuario. Por defecto "../"
 * @return void
 */
function logout(string $to = "../")
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
