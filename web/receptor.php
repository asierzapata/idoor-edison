<?php
include_once "conexion.php";

$conexion = new conexion();



$conexion->tareapendiente($conexion->getIdAlumno($_GET['id_alumno']));

$conexion->horario_alumno($conexion->getIdAlumno($_GET['id_alumno']));
$conexion->notas($conexion->getIdAlumno($_GET['id_alumno']));