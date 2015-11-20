<?php
	include_once ("../conexion.php");

	/*$conexion = new conexion();
	$conexion->POST_Asignaturas_Y_Grupos_Profesor(1);*/
	
	if(isset($_POST['id_asig'])) {
		
		$ciudades = array();
		//lo que recibimos en ese $_POST es id_asignatura-id_profesor toca desmontarlo
		$id_profesor = explode("-",$_POST['id_asig']);
		$id_asignatura = $id_profesor[0];  
		$id_profesor = $id_profesor[1];
		$conexion = new conexion();
		$mysqli = $conexion->datos_mysqli();
        //$result = $mysqli->query("SELECT idciudad,nombre FROM ciudades WHERE idpais = ".$_POST['id_grupo_asignatura']); 

        $result = $mysqli->query("SELECT numero,id FROM grupo_asignatura WHERE id_asignatura = ".$id_asignatura." AND id_profesor=".$id_profesor." GROUP BY numero");
		while($row = $result->fetch_assoc()){
			$ciudad = new grupo($row['id'], $row['numero']);
		    array_push($ciudades, $ciudad);
		    
		}
		echo json_encode($ciudades);
	}
	
	class grupo {
		public $id;
		public $nombre;

		function __construct($id, $nombre) {
			$this->id = $id;
			$this->nombre = $nombre;
		}
	}
?>