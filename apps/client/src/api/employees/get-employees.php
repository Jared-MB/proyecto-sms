<?php

require_once __DIR__ . '/../../core/services/database.php';

$area = $_GET['area'];
$sql = "SELECT APPEMP,APMEMP,NOMEMP,IDEPER FROM PER,EMP,CAR WHERE EMPPER=IDEEMP && CARPER=IDECAR && COOCAR='$area' && FECFIN IS NULL ORDER BY NOMEMP";

$result = $db->query($sql);

$employees = $result->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($employees);
