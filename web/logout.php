<?php
session_start();
session_destroy();
echo "hola";
header ("Location: index.php");
?>