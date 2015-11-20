<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <title>Login idoorweb screen</title>
    <script src="http://s.codepen.io/assets/libs/modernizr.js" type="text/javascript"></script>


    
    <link rel="stylesheet" href="css/normalize.css">

    <link rel='stylesheet prefetch' href='https://raw.githubusercontent.com/daneden/animate.css/master/animate.css'>

        <link rel="stylesheet" href="css/style.css">

    
    
    
  </head>

  <body>

    <div class="container">
    <div class="bg-img"></div>
    <div class="header">
        <div class="loading">
            <div class="block"></div>
            <div class="block"></div>
            <div class="block"></div>
            <div class="block"></div>
        </div>
        <h1>iDoorWeb</h1>
    </div>
    <div class="main">
        <div class="login">
            <form action="controlador.php" method="POST">
                <?php

                    if(isset($_POST['error'])) {
                        echo "Revisa tus datos de nuevo";
                    }

               ?>
                <input id="login_u" name="username" required="required" type="text" placeholder="Username" />

                <input id="login_p" name="password" required="required" type="password" placeholder="Password" />
                
                <button type="submit" value="Login" />Login</button>


                <span class="form-toggle">Registrarse</span>
            </form>
        </div>
        <div class="register">
            <form>
                <input id="firstname" name="firstname" required="required" type="text" placeholder="First name" />
                <input id="lastname" name="lastname" required="required" type="text" placeholder="Last name" />
                <input id="email" name="email" required="required" type="enail" placeholder="Email" />
                <input id="username" name="username" required="required" type="text" placeholder="Username" />
                <input id="password" name="password" required="required" type="password" placeholder="Password" />
                <!--<select id="firstname" name="select-grupo">
                    <option value="0">Seleccione sus asignaturas</option>
                    <option value="1">Curs 1A</option>
                    <option value="2">Curs 1B</option>
                    <option value="3">Curs 2A</option>
                    <option value="4">Curs 2B</option>
                    <option value="5">Curs 3A</option>
                    <option value="6">Curs 3B</option>
                    <option value="7">Curs 4A</option>
                    <option value="8">Curs 4B</option>
                </select>
                <select id="cboGrupos" name="select-grupo">
                    <option value="0">Seleccione su grupos</option>
                    <option value="1">Grup 10</option>
                    <option value="2">Grup 20</option>
                    <option value="3">Grup 30</option>
                    <option value="4">Grup 40</option>
                    <option value="5">Grup 50</option>
                    <option value="6">Grup 60</option>
                </select>-->
                <button type="submit" value="Login" />Register</button>
                <span class="form-toggle">Return to Login</span>
            </form>
            
        </div>
    </div>
    <div class="footer">
        <ul class="footer-nav">
            <li class="link">FAQ</li>
            <li class="link">About Us</li>
            <li class="link">Contact Us</li>
            <li class="link">Privacy Policy</li>
        </ul>
      <!--<p class="disclaimer"><b>Disclaimer</b> Every effort is made to keep the website up and running smoothly. However, we takes no responsibility for, and will not be liable for, the website being temporarily unavailable due to technical issues beyond our control.</p>-->
    </div>
</div>
    <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

        <script src="js/index.js"></script>

    
    
    
  </body>
</html>
