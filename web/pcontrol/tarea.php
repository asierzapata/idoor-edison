<?php
    include_once ("../conexion.php");
    session_start();
?>


<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>PBE</title>
    <link rel='stylesheet prefetch' href='http://fonts.googleapis.com/css?family=Roboto'>
    <link rel="stylesheet" href="css/style.css">
   <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
    <script>
    /*ESTE TROZODE AQUI SE ENCARGA DE VARIAR EL SCROLL SEGUN EL PROFE QUE SEAS*/
        $(document).ready(function(){
            $("#cboAsignaturas").change(function() {
                var asignatura = $(this).val();
                
                
                if(asignatura.indexOf('-') != -1)
                {
                    var datos = {
                        id_asig : $(this).val()
                    };
                    console.log( JSON.stringify(datos) );

                    

                    $.post("grupo.php", datos, function(grupos) {
                        
                        var $comboGrupos = $("#cboGrupos");
                        $comboGrupos.empty();
                        $.each(grupos, function(index, grupo) {
                            //
                            $comboGrupos.append("<option>" + grupo.nombre + "</option>");
                        });
                    }, 'json');
                }
                else
                {
                    var $comboGrupos = $("#cboGrupos");
                    $comboGrupos.empty();
                    $comboGrupos.append("<option>Seleccione una asignatura</option>");
                }
            });
        });

    </script>

        
    
        <style>
      body {
    font-family: 'Roboto', Arial, sans-serif;
    background-color: #ebebeb;
    overflow-x: hidden;
    text-align: center;
}

header {
    width: 120%;
    height: 50px;
    margin-left: -20px;
    background-color: #00b3a0;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}

header > nav > div {
    float: left;
    width: 17.2%;
    height: 100%;
    position: relative;
}

header > nav > div > a {
    text-align: center;
    width: 100%;
    height: 100%;
    display: block;
    line-height: 50px;
    color: #fbfbfb;
    transition: background-color 0.2s ease;
    text-transform: uppercase;
}

header > nav > div:hover > a {
    background-color: rgba(0, 0, 0, 0.1);
    cursor: pointer;
}

header > nav > div > div {
    display: none;
    overflow: hidden;
    background-color: white;
    min-width: 200%;
    position: absolute;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
    padding: 10px;
}

header > nav > div:not(:first-of-type):not(:last-of-type) > div {
    left: -50%;
    border-radius: 0 0 3px 3px;
}

header > nav > div:first-of-type > div {
    left: 0;
    border-radius: 0 0 3px 0;
}

header > nav > div:last-of-type > div {
    right: 0;
    border-radius: 0 0 0 3px;
}

header > nav > div:hover > div {
    display: block;
}

header > nav > div > div > a {
    display: block;
    float: left;
    padding: 8px 10px;
    width: 46%;
    margin: 2%;
    text-align: center;
    background-color: #f44355;
    color: #fbfbfb;
    border-radius: 2px;
    transition: background-color 0.2s ease;
}

header > nav > div > div > a:hover {
    background-color: #212121;
    cursor: pointer;
}

h1 {
    margin-top: 100px;
    font-weight: 100;
}

p {
    color: #aaa;
    font-weight: 300;
}

@media (max-width:600px) {
    header > nav > div > div > a {
        margin: 5px 0;
        width: 100%;
    }
    header > nav > div > a > span {
        display: none;
    }
}
    </style>

    
        

    
  </head>
  <body>
  

    <header>
    <nav>
        <div>
            <a><span>Tab </span>1</a>
            <div>
                <a>Link 1</a>
                <a>Link 2</a>
                <a>Link 3</a>
                <a>Link 4</a>
                <a>Link 5</a>
                <a>Link 6</a>
            </div>
        </div>
        <div>
            <a href="tarea.php"><span> Nova Tarea </span></a>
            
        </div>
        <div>
            <a  href="table/index.html"><span>Pujar notes</span></a>
            
        </div>
        <div>
            <a><span>Tab </span>4</a>
            
        </div>
        <div>
            <a href="../logout.php"><span>Cerrar sesion </span></a>
            
        </div>
    </nav>
</header>


    </div>
    <div class="container">
        <?php
            if(isset($_POST['select-asignatura'])){
                $conexion = new conexion();
                session_start();
                echo $_Session['pruebas'];
                $conexion->guardar_tarea($_POST['select-asignatura'],$_POST['select-grupo'],$_POST['tarea'],$_POST['fecha-entrega']);
                ?>
                <script>alert("Tarea creada y guardadacorrectamente")</script>
                <!--<font color="red">Tarea ok</font>-->
                <?php
            }            
        ?>
      <h2>Nova Tasca</h2>
      
      <form action="tarea.php" method="POST">
        <!--Queria empezar a montar este apartado, falta el check-box y el select tag por meter y luego php y a montar -->
        <div style="color:#999;font-size:18px;margin-left: -400px;margin-top:-40px;">Asignatura<br></div>
        <div style="margin-left: -200px; position:relative;">
            <select id="cboAsignaturas" name="select-asignatura">

                <option value="0">Seleccione una Asignatura</option>
                <?php
                    $conexion = new conexion();
                    //RECUERDA PASAR EL ID DEL PROFE POR PARAMETRO
                    $array = $conexion->get_Asignaturas_Y_Grupos_Profesor($_SESSION['id_user']);
                    for($i=0;$i<=count($array)-1;$i++){
                            echo '<option value="'.$array[$i]['id'].'">'.$array[$i]['nombre_asignatura'].'</option>';        
                    }
                ?>
                    
                
            </select>
          

        </div>
        <div style="color:#999;font-size:18px;margin-left: -450px;margin-top:15px;">Grup<br></div>
        <div style="margin-left: -200px; position:relative; margin-top:0px">
            <select id="cboGrupos" name="select-grupo">
                <option value="0">Seleccione un grupo</option>
            </select>
      

    </div>

    <div class="group1">      
      <input type="textarea"  name="tarea" required>
      <span class="highlight"></span>
      <span class="bar"></span>
      <label>Descripci&oacute; de la tarea</label>
    </div>
    <input type="date" name="fecha-entrega" step="1" min="<?php echo date("Y-m-d");?>" max="2016-12-31" value="Data d'entrega" required="required">
    <br>
    <input type="submit" class="btn btn-primary btn-lg box-shadow--6dp">
    
    
    </form>
  
</div>

    
    
    
  
    
        <!--<h1>Nueva Tarea</h1>
        <br>
        <form action="helper.php" method="POST" id="formulario">
            Asignatura: <br>
            <input type="checkbox" name="rp" value=1 />Radiaci&oacute; i propagacio
            <input type="checkbox" name="icom" value=1 />Introducció a les comunicacions<br />
            
            Grupo: <br>
            <input type="checkbox" name="g11" value=1 />Grup 11
            <input type="checkbox" name="g12" value=1 />Grup 12<br />
            <input type="checkbox" name="g12" value=1 />Item 4<br />class="checkbox">
            
            
            Tarea: <br>
            <input type="text" placeholder="usuario" name="tarea"/>
            <br>
            
            <!--<input type="text" placeholder="usuario" name="txtusuario" />
            <br>
            <input type="password" placeholder="pass" name="txtpassword" />
            <br>
            <input type="submit" value="submit" name="entrar" />
        </form>-->
    </body>
</html>
