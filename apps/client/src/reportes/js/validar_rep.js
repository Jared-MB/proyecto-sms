$(() => {
	$("#form_rep").validate({
		rules: {
			area: { required: true },
			emp: { required: true },
			fecsus: { required: true },
			fecrep: { required: true },
			lugsus: { required: true },
			obs: { maxlength: 300 },
		},

		messages: {
			area: "Elija un área",
			emp: "Elija un nombre",
			fecsus: "Elija una fecha de suceso",
			fecrep: "Elija una fecha de reporte",
			lugsus: "Elija un lugar del suceso",
			obs: {
				maxlength: "Máximo 100 caracteres",
			},
		},

		submitHandler: (form) => {
			$("#enviar").attr("disabled", true).val("Enviando...");

			const payload = {
				CONREP: $("#con").val(),
				FECEVE: $("#fecsus").val(),
				FECREP: $("#fecrep").val(),
				LUGREP: $("#lugsus").val(),
				OBSREP: $("#obs").val(),
				FREREP: $("#freeve").val(),
				PERREP: $("#emp").val(),
				CANREP: $("#area").val(),
			};

			$.ajax({
				type: "POST",
				url: "http://127.0.0.1:5001/rep",
				headers: {
					Authorization: "Bearer MI_TOKEN_SEGURO_12345",
				},
				contentType: "application/json",
				data: JSON.stringify(payload),
				success: (data) => {
					console.log("Guardado!", data);
					location.reload();
				},
				error: (xhr) => {
					console.error(xhr.responseText);
					alert("Error al guardar REP");
				},
			});
		},
	});
});
