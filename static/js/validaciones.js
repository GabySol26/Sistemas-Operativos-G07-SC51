function valtelef(inputTelefono) {
    var telefono = inputTelefono.value.trim();
    var telefonoRegex = /^[0-9]{9}$/;

    if (!telefonoRegex.test(telefono)) {
        document.getElementById("telefonoHelpBlock").innerHTML = "El número de celular debe contener 9 dígitos numéricos";
    } else {
        document.getElementById("telefonoHelpBlock").innerHTML = "";
    }
}

function valdni(inputDni) {
    var dni = inputDni.value.trim();
    var dniRegex = /^[0-9]{8}$/;

    if (!dniRegex.test(dni)) {
        document.getElementById("dniHelpBlock").innerHTML = "El DNI debe contener 8 dígitos numéricos";
    } else {
        document.getElementById("dniHelpBlock").innerHTML = "";
    }
}

function valcole(inputCole)
{
    var colegio = inputCole.value.trim();
    var colegioRegex = /^[0-9]{6}$/;

    if (!colegioRegex.test(colegio)) {
        document.getElementById("colegioHelpBlock").innerHTML = "El código del número colegiado debe contener 6 dígitos numéricos";
    }
    else {
        document.getElementById("colegioHelpBlock").innerHTML = "";
    }

}

function validateDosis() {
    const dosisInput = document.getElementsByName("dosis")[0];
    const dosisError = document.getElementById("dosis-error");
    const dosisValue = dosisInput.value.trim();

    const dosisRegex = /^[0-9]+$/;
    if (!dosisRegex.test(dosisValue)) {
        dosisError.textContent = "La dosis debe ser un número entero";
    } else {
        dosisError.textContent = "";
    }
}
