<?php
include_once ("../conexion.php");

$conexion = new conexion();
echo $select_asignatura = $_POST['select-asignatura'];
echo "<br>";
echo $select_grupo = $_POST['select-grupo'];
echo "<br>";
echo $tarea = $_POST['tarea'];
echo "<br>";
echo $fecha_entrega = $_POST['fecha-entrega'];
//select_asignatura lleva dentro id_asignatura-id_profesor
$conexion->guardar_tarea($select_asignatura,$select_grupo,$tarea,$fecha_entrega);
?>
<script>alert("Tarea creada")</script>
<?php


/*
$tarea = $_POST["tarea"];
$data = $_POST["entrega"];
$subject = $_POST["subject"];
echo "El profesor ha elegido la asignatura de: ".$subject."<br>";
echo "La tarea propuesta es: ".$tarea."<br>";
echo "La fecha de entrega es: ".$data."<br>";




/*$array = array(
    "rp" => "Radiació y propagacio",
    "icom" => "Introducció a les telecomunicacions",
);
if(IsChecked("rp","yes")){
    echo "sep, rp activado";
}else{
    echo "rp no esta activado";
}
echo "<br>";
if(IsChecked("icom","yes")){
    echo "sep, icom activado";
}else{
    echo "icom no esta activado";
}
function IsChecked($chkname,$value)
    {
        if(!empty($_POST[$chkname]))
        {
            echo $valor = $_POST[$chkname];
                if($valor)
                {
                    return true;
                }
        }else{
            echo "no entrado";
        }
        return false;
    }


*/

/*
if(isset($_POST['formWheelchair']) && 
   $_POST['formWheelchair'] == 'Yes') 
{
    echo "Need wheelchair access.";
}
else
{
    echo "Do not Need wheelchair access.";
} 

*/
?>
