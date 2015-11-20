<?php 



include_once "conexion.php";

$conexion = new conexion();

$conexion->get_Asignaturas_Y_Grupos_Profesor(1);