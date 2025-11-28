$(function () {

    $("#form_lug").validate({
        
        rules: {
            nom: {
                required: true,
                maxlength: 100
            }
        },

        messages: {
            nom: {
                required: "Es necesario introducir el nombre de un lugar",
                maxlength: "Máximo 100 caracteres"
            }
        },

        submitHandler: function (form) {

            $("#enviar_lug")
                .prop("disabled", true)
                .val("Enviando...");

            const payload = {
                nom: $("#nom").val()
            };

            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5001/lug",   // ⬅️ NUEVO: tu servicio Flask
                headers: {
                    "Authorization": "Bearer MI_TOKEN_SEGURO_12345"
                },
                contentType: "application/json",
                data: JSON.stringify(payload),

                success: function (response) {
                    console.log("Guardado:", response);
                    cerrarventana('.ventana_3');
                    location.reload();
                },

                error: function (xhr) {
                    console.error("Error:", xhr.responseText);
                    alert("Error al guardar lugar");
                    $("#enviar_lug")
                        .prop("disabled", false)
                        .val("Enviar");
                }
            });
        }
    });

});
