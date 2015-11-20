<?php
session_start();
include_once ("conexion.php");

$conexion = new conexion();


$array = $conexion->horario_alumno(1);
var_dump(json_encode($array));




