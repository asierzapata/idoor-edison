<?php

	function obtenerTodosLosPaises() {
		$paises = array();
		$datos = datos_bd();
		$mysqli = new mysqli("localhost", $datos['user'],$datos['pw'],$datos['nombre_bd']) or die ("Error al conectar.");
        $result = $mysqli->query("SELECT id_asignatura FROM grup_asignatura WHERE id_profesor = ".$_GET['idprofe']);
        while($fila = $result->fetch_assoc()){
            $aux = $mysqli->query("SELECT nombre FROM asignaturas WHERE id=".$fila['id_asignatura']." LIMIT 1");
            $aux_fila = $aux->fetch_row();
            var_dump($aux_fila);
            $i++;
        }
		while($row = $result->fetch_assoc()){
			$pais = new profe_asignatura($row['idpais'], $row['nombre']);
		    array_push($paises, $pais);
		}
		$mysqli->close();

		return $paises;
	}
	/*function nuevaasignatura($array_idasignaturas,$id){
        for($j=0;$j<count($array_idasignaturas);$j++) {
            if($array_idasignaturas[$j]==$id){
                return false;
            }
        }
        return true;

    }*/

	class profe_asignatura {
		public $id;
		public $id_asignatura;

		function __construct($id, $nombre) {
			$this->id = $id;
			$this->nombre = $nombre;
		}
	}
?>