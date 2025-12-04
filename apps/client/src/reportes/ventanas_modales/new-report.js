async function loadAreas() {
	const areaSelect = document.getElementById("area-select");

	areaSelect.addEventListener("change", loadEmployees);

	const response = await fetch("query/con_coo.php");
	const data = await response.json();

	let options = "<option selected='selected' value=''>--ELEGIR--</option>";
	for (let i = 0; i < data.length; i++) {
		options += `<option value="${data[i].IDECOO}">${data[i].NOMCOO}</option>`;
	}

	areaSelect.innerHTML = options;
}

async function loadEmployees() {
	const employeesSelect = document.getElementById("employees-select");

	const response = await fetch(
		"/api/employees/get-employees?area=" +
			document.getElementById("area-select").value,
	);
	const data = await response.json();

	let options = "<option selected='selected' value=''>--ELEGIR--</option>";
	for (let i = 0; i < data.length; i++) {
		options += `<option value="${data[i].IDEPER}">${data[i].NOMEMP} ${data[i].APPEMP} ${data[i].APMEMP}</option>`;
	}

	employeesSelect.innerHTML = options;
}

async function loadLocations() {
	const locationsSelect = document.getElementById("locations-select");

	const response = await fetch("query/con_lug.php");
	const data = await response.json();

	let options = "<option selected='selected' value=''>--ELEGIR--</option>";
	for (let i = 0; i < data.length; i++) {
		options += `<option value="${data[i].IDELUG}">${data[i].NOMLUG}</option>`;
	}

	locationsSelect.innerHTML = options;
}

function createTableFilter() {
	const filtersConfig = {
		base_path: "../../TableFilter-master/dist/tablefilter/",
		col_0: "select",
		col_4: "select",
		col_5: "select",
		col_6: "select",
		col_7: "select",
		col_9: "none",
		col_10: "none",

		alternate_rows: true,
		rows_counter: true,
		btn_reset: true,
		loader: true,
		mark_active_columns: true,
		highlight_keywords: true,
		no_results_message: true,
		col_types: ["string", "string"],
		extensions: [
			{
				name: "sort",
				images_path: "../../TableFilter-master/dist/tablefilter/style/themes/",
			},
		],
	};

	return new TableFilter("tabla_rep", filtersConfig);
}

async function submitReport(e) {
	const $sendButton = document.getElementById("enviar");
	$sendButton.disabled = true;
	$sendButton.value = "Enviando...";

	const payload = new FormData(e);

	const response = await fetch("/api/reports/upload", {
		method: "POST",
		body: payload,
	});

	const data = await response.json();

	if (response.ok) {
		console.log("Guardado!", data);
		location.reload();
	} else {
		console.error(data);
		alert("Error al guardar REP");
	}
}

document.addEventListener("DOMContentLoaded", async () => {
	await Promise.all([loadAreas(), loadLocations()]);

	const tableFilter = createTableFilter();
	tableFilter.init();

	$("#form_rep").validate({
		rules: {
			"area-select": { required: true },
			emp: { required: false },
			fecsus: { required: true },
			fecrep: { required: true },
			"locations-select": { required: true },
			obs: { maxlength: 300 },
		},

		messages: {
			"area-select": "Elija un área",
			emp: "Elija un nombre",
			fecsus: "Elija una fecha de suceso",
			fecrep: "Elija una fecha de reporte",
			"locations-select": "Elija un lugar del suceso",
			obs: {
				maxlength: "Máximo 100 caracteres",
			},
		},

		submitHandler: submitReport,
	});
});
