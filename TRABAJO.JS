// =======================
// CLASE PADRE: Persona
// =======================
class Persona {
    constructor(nombre) {
        this.nombre = nombre;
    }

    registrar() {
        return `Registrada persona: ${this.nombre}`;
    }
}

// =======================
// CLASE HIJA: Estudiante
// =======================
class Estudiante extends Persona {

    constructor(nombre, nota1, nota2, nota3) {
        super(nombre);
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
    }

    calcularPromedio() {
        return (this.nota1 + this.nota2 + this.nota3) / 3;
    }

    evaluacion() {
        let prom = this.calcularPromedio();
        return prom >= 3.0 ? "Aprobado" : "Reprobado";
    }
}

// =======================
// LISTA GLOBAL
// =======================
let estudiantes = [];

// =======================
// FUNCIÓN PARA REGISTRAR
// =======================
function registrarEstudiante() {

    let nombre = document.getElementById("nombreEst").value;
    let n1 = Number(document.getElementById("nota1").value);
    let n2 = Number(document.getElementById("nota2").value);
    let n3 = Number(document.getElementById("nota3").value);

    let nuevo = new Estudiante(nombre, n1, n2, n3);
    estudiantes.push(nuevo);

    mostrarLista();
}

// =======================
// MOSTRAR EN PANTALLA
// =======================
function mostrarLista() {

    let zona = document.getElementById("lista");
    zona.innerHTML = ""; // limpiar

    estudiantes.forEach(est => {
        zona.innerHTML += `
            <p>
                <strong>${est.nombre}</strong><br>
                Promedio: ${est.calcularPromedio().toFixed(2)}<br>
                Estado: <span class="${est.evaluacion()}">${est.evaluacion()}</span>
            </p>
        `;
    });
}
