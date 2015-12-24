<?php
include_once "conexion.php";

$conexion = new conexion();

	


if(isset($_GET['modo'])){
	$conexion->horario_alumno($conexion->getIdAlumno($_GET['id_alumno']));
}elseif(isset($_GET['amigos'])){
	$conexion->get_amigos($conexion->getIdAlumno($_GET['id_alumno']),true);
}
elseif(isset($_GET['friend'])){
	$conexion->add_friend($conexion->getIdAlumno($_GET['id_alumno']),$conexion->getIdAlumno($_GET['friend']));

}elseif(isset($_GET['last_check'])){
	$conexion->get_amigos($conexion->getIdAlumno($_GET['id_alumno']),false);

}else{
	$conexion->registrar_lugar($conexion->getIdAlumno($_GET['id_alumno']),$_GET['lugar']);
	$conexion->tareapendiente($conexion->getIdAlumno($_GET['id_alumno']));
	$conexion->horario_alumno($conexion->getIdAlumno($_GET['id_alumno']));
	$conexion->notas($conexion->getIdAlumno($_GET['id_alumno']));
}



