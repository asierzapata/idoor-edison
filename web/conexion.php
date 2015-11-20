

<?php
class conexion{
    
    function get_Asignaturas_Y_Grupos_Profesor($id_profesor){
        echo $id_profesor;
        $mysqli = $this->datos_mysqli();
        $resultado = $mysqli->query("SELECT id_asignatura,numero,id FROM grupo_asignatura WHERE id_profesor=".$id_profesor);
        $asignaturas=array();
        $i=0;
        $array_idasignaturas =array(); 
        while($fila = $resultado->fetch_row()){
            $aux = $mysqli->query("SELECT nombre FROM asignaturas WHERE id=".$fila[0]." LIMIT 1");
            $aux_fila = $aux->fetch_row();
            if($this->nuevaasignatura($array_idasignaturas,$fila[0])){
                echo $asignaturas[$i]['id'] = $fila[0]."-".$id_profesor."-".$fila[2];
                $asignaturas[$i]['nombre_asignatura'] = utf8_encode($aux_fila[0])/*." - Grup_asignatura: ".$fila[2]*/;
                array_push($array_idasignaturas, $fila[0]); 
                $i++;
            }  
        }
        
        return $asignaturas;
    }


    function nuevaasignatura($array_idasignaturas,$id){
        for($j=0;$j<count($array_idasignaturas);$j++) {
            if($array_idasignaturas[$j]==$id){
                return false;
            }
        }
        return true;

    }
    

    function guardar_tarea($select_asignatura,$select_grupo,$tarea,$fecha_entrega){
        $aux = explode("-", $select_asignatura);
        //$id_grupo_asignatura = $aux[2];
        $id_profesor = $aux[1];
        $id_asignatura = $aux[0];
        echo $id_profesor."-".$id_asignatura."-".$select_grupo;
        //var_dump($select_grupo);
        $mysqli = $this->datos_mysqli();
        
        $resultado = $mysqli->query("SELECT id FROM grupo_asignatura 
            WHERE numero=".$select_grupo." AND id_asignatura=".$id_asignatura);
        $fila = $resultado->fetch_row();
        echo "<br>";
        $id_grupo_asignatura = $fila[0];
        $mysqli->query("INSERT INTO `tarea_alumno` (`id_profesor`,`id_grupo_asignatura`,`tarea`,`id_asignatura`,`fecha_entrega`) 
            VALUES ('$id_profesor','$id_grupo_asignatura','$tarea','$id_asignatura','$fecha_entrega');");
    }

    function getIdAlumno($codigo){
        $mysqli = $this->datos_mysqli();
        $resultado = $mysqli->query("SELECT id,nombre,codigo FROM alumno");
        $encontrado = false;
        while($aux_user = $resultado->fetch_assoc()){
            if(stripos($aux_user['codigo'],$codigo)!==FALSE){
                $encontrado = true;
                break;
            }
        }
        if($encontrado){
            return $aux_user['id'];
        }else{
            ?>
            <script>alert("No hay ningun usuario en nuestra base de datos con ese id, por favor registrate en idoorweb.com")</script>
            <?php
            
            exit;
            return NULL;
        }
        
    }
    function tareapendiente($id_alumno){
        $mysqli = $this->datos_mysqli();
        $grupos_asignaturas = $mysqli->query("SELECT id_grupo_asignatura FROM asignatura_alumno 
            WHERE id_alumno=".$id_alumno);
        $tareas_todas = array();
        $i=0;
        if($grupos_asignaturas!=FALSE){
            while($fila = $grupos_asignaturas->fetch_row()){
                $tareas = $mysqli->query("SELECT tarea,fecha_entrega,id_asignatura FROM tarea_alumno WHERE id_grupo_asignatura=".$fila[0]);
                if($tareas!=FALSE){
                    while($aux_tarea = $tareas->fetch_assoc()){
                        
                        $nombre_asignatura = $mysqli->query("SELECT siglas FROM asignaturas WHERE id=".$aux_tarea['id_asignatura']);
                        if($nombre_asignatura!=FALSE){
                            $nombre_asignatura = $nombre_asignatura->fetch_row();
                            $nombre_asignatura = $nombre_asignatura[0];
                        }else{
                            echo "Quiere decir que no hemos encontrado nombre de la asignatura, eso es muy malo";
                        }                        
                        $tareas_todas['tareas'][$i]['siglas_asignatura'] = $nombre_asignatura;
                        $tareas_todas['tareas'][$i]['tarea'] = $aux_tarea['tarea'];
                        $tareas_todas['tareas'][$i]['entrega'] = $aux_tarea['fecha_entrega'];
                        ++$i;
                    }
                            //TA COMPLICADO CONCENTRATE Y SIGUE
                    
                }else{
                    echo "No hay ninguna tarea para las asignaturas que estoy matriculado";
                }
                
            }
        }else{
            echo "No tengo asignaturas asignadas";
        }
        echo json_encode($tareas_todas);
    }
    function horario_alumno($id_alumno){
        $conexion = new conexion();
        $mysqli = $this->datos_mysqli();
        $retorno = array();
        $grupos_asignaturas = $mysqli->query("SELECT id_grupo_asignatura FROM asignatura_alumno WHERE id_alumno=".$id_alumno);
        //1,3,4,5,6,7,8,9 id de grupo_asignatura
        while($fila = $grupos_asignaturas->fetch_row()){
            //el primero es el id=1
            $horario = $mysqli->query("SELECT id_asignatura,aula,horario FROM grupo_asignatura WHERE id=".$fila[0]);
            //No hace falta while porque solo habrá uno
            $aux_horario = $horario->fetch_assoc();    
            $aux_horario_dividido = explode("-",$aux_horario['horario']);
            $siglas = $conexion->get_nombre_sigla_asignatura($aux_horario['id_asignatura']);
            if($aux_horario_dividido[0]==1){
                $dia = "Lunes";
            }
            elseif($aux_horario_dividido[0]==2){
                $dia = "Martes";
            }
            elseif($aux_horario_dividido[0]==3){
                $dia = "Miercoles";
            }
            elseif($aux_horario_dividido[0]==4){
                $dia = "Jueves";
            }
            elseif($aux_horario_dividido[0]==5){
                $dia = "Viernes";
            }else{echo "A TOMAR POR ... ALGO HA IDO MAL";}
            $retorno['horario'][$aux_horario_dividido[1]][$dia] = $siglas['siglas']." ".$aux_horario['aula'];       

        }
        // echo "{\"horario\"{";
            /*for($i=8;$i<=20;$i++){
                if(isset($retorno['horario'][$i])){
                    echo "\"".$i."\":{";
                    for($j=1;$j<=5;$j++){
                        if(isset($retorno['horario'][$i][$j])){
                            if($j==5){
                                 echo $conexion->traductor_dias($j).":"."\"".$retorno['horario'][$i][$j]."\"";
                            }else{
                                 echo $conexion->traductor_dias($j).":"."\"".$retorno['horario'][$i][$j]."\",";
                            }
                           
                        }else{
                            if($j==5){
                                //echo $conexion->traductor_dias($j).":"."\"libre\"";
                            }else{
                                //echo $conexion->traductor_dias($j).":"."\"libre\",";
                            }
                            
                        }
                    }
                }
                
                if($i==20){
                     echo "}";
                }else{
                    echo "},";
                }
            }
            echo "}";*/
        
        echo json_encode($retorno);
    }

    function traductor_dias($aux_horario_dividido){
        if($aux_horario_dividido==1){
                $dia = "\"Lunes\"";
        }
        elseif($aux_horario_dividido==2){
            $dia = "\"Martes\"";
        }
        elseif($aux_horario_dividido==3){
            $dia = "\"Miercoles\"";
        }
        elseif($aux_horario_dividido==4){
            $dia = "\"Jueves\"";
        }
        elseif($aux_horario_dividido==5){
            $dia = "\"Viernes\"";
        }else{echo "A TOMAR POR ... ALGO HA IDO MAL";}
        return $dia;
    }
    function notas($id_alumno){
        $conexion = new conexion();
        $mysqli = $this->datos_mysqli();
        $retorno = array();
        $notas_alumno = $mysqli->query("SELECT id_grupo_asignatura,concepto,nota FROM notas WHERE id_alumno=".$id_alumno);
        echo "NOTAS{";
        while($fila = $notas_alumno->fetch_assoc()){
            $siglas_asignatura = $conexion->get_nombre_sigla_asignatura($fila['id_grupo_asignatura']);
            $siglas_asignatura = $siglas_asignatura['siglas'];
            echo $siglas_asignatura.":".$fila['concepto'].":".$fila['nota']."/"; 
        }
        echo "}";


    }

    function get_nombre_from_id_grupo_asignatura($id_grupo_asignatura){
        $conexion = new conexion();
        $mysqli = $this->datos_mysqli();
        $retorno = array();
        $aux = $mysqli->query("SELECT id_asignatura FROM grupo_asignatura WHERE id=".$id_grupo_asignatura);
        $fila = $aux->fetch_row();
        $datos = $conexion->get_nombre_sigla_asignatura($fila[0]);
        return $datos;

        
    }
        
    

    function get_nombre_sigla_asignatura($id_asignatura){
        $mysqli = $this->datos_mysqli();
        $asignaturas = $mysqli->query("SELECT nombre,siglas FROM asignaturas WHERE id=".$id_asignatura);
        $fila = $asignaturas->fetch_assoc();
        $retorno['siglas'] = $fila['siglas'];
        $retorno['nombre'] = $fila['nombre'];
        $mysqli->close();
        return $retorno;
    }
    
    
    function datos_mysqli(){
        $datos['user'] = "u388114445_admin";
        $datos['pw'] = "cambiame1234";
        $datos['nombre_bd'] = "u388114445_pbe";
        $mysqli = new mysqli("localhost", $datos['user'],$datos['pw'],$datos['nombre_bd']) or die ("Error al conectar.");
        return $mysqli;
    }
}