<?php
	include_once ("conexion.php");

	$conexion = new conexion();
	$controlador = new controlador();
	session_start();
	if(isset($_POST['username'])) {
        $controlador->revisa_login($_POST['username'],$_POST['password']);
    }else{
    	echo "no entrado";
    }


	
	
	class controlador {
		public $id;
		public $nombre;
		

		function revisa_login($user,$pass) {
			echo $user.$pass;
			$conexion = new conexion();
			$mysqli = $conexion->datos_mysqli();
			$result = $mysqli->query("SELECT id,nombre,user,pass FROM alumno ");
			$id="vacia";

			while($fila=$result->fetch_assoc()){
				if($fila['user']  == $user && $fila['pass']  == $pass){
					$id = $fila['id'];
					$_SESSION["nombre_user"] = $fila['nombre'];
					$es_profe = false;
				}

			}
			if($id == "vacia"){
				$result = $mysqli->query("SELECT id,nombre,user,pass FROM profesor ");
				while($fila=$result->fetch_assoc()){
					if($fila['user']  == $user && $fila['pass']  == $pass){
						$id = $fila['id'];
						$_SESSION["nombre_user"] = $fila['nombre'];
						$es_profe = true;
					}
				}
			}
			if($id == "vacia"){
				echo "incorrecta";
				$_SESSION["id_user"] = "vacia";
				header ("Location: index.php");

			}else{
				$_SESSION["id_user"] = $id;
				if($es_profe){
					header ("Location: pcontrol/");
				}else{
					header ("Location: index.php");
				}
			}
			


			//header ("Location: http://www.cristalab.com");
		}
		




		function gethtml($url){
	        $ch = curl_init($url);  // Initialise a cURL handle
	        curl_setopt($ch, CURLOPT_HEADER, FALSE);
	        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, TRUE);
	        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	        curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
	        $results = curl_exec($ch);  // Execute a cURL request
	        curl_close($ch); 
	        return $results;
    	}
	}
?>