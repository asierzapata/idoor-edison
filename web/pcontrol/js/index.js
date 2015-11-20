$(document).ready(function(){

    // cada vez que se cambia el valor del combo
    $("#grupos").change(function() {

        // obtenemos el valor seleccionado
        var id_asignatura = $(this).val();

        // si es 0, no es un país
        if(id_asignatura > 0)
        {
            //creamos un objeto JSON
            var datos = {
                idPais : $(this).val()  
            };

            // utilizamos la función post, para hacer una llamada AJAX
            $.post("ciudad.php", datos, function(ciudades) {

                // obtenemos el combo de ciudades
                var $comboCiudades = $("#cboCiudades");

                // lo vaciamos
                $comboCiudades.empty();

                // iteramos a través del arreglo de ciudades
                $.each(ciudades, function(index, cuidad) {

                    // agregamos opciones al combo
                    $comboCiudades.append("<option>" + cuidad.nombre + "</option>");
                });
            }, 'json');
        }
        else
        {
            // limpiamos el combo e indicamos que se seleccione un país
            var $comboCiudades = $("#cboCiudades");
            $comboCiudades.empty();
            $comboCiudades.append("<option>Seleccione un país</option>");
        }
    });
}); 