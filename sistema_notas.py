from estudiante import Estudiante
from profesor import Profesor

class SistemaNotas:
    def __init__(self):
        self.estudiantes = []
        self.profesores = []

    def registrar_estudiantes(self):
        print("=== REGISTRO AUTOMÁTICO DE ESTUDIANTES ===")
        cantidad = int(input("¿Cuántos estudiantes desea registrar? : "))

        for i in range(cantidad):
            nombre = input(f"Nombre del estudiante {i+1}: ")
            estudiante = Estudiante(id_estudiante=i+1, nombre=nombre)
            self.estudiantes.append(estudiante)

        print("Estudiantes registrados exitosamente.\n")

    def registrar_profesores(self):
        print("=== REGISTRO DE PROFESORES ===")
        cantidad = int(input("¿Cuántos profesores desea registrar? : "))

        for i in range(cantidad):
            nombre = input(f"Nombre del profesor {i+1}: ")
            materia = input("Materia que dicta: ")

            profesor = Profesor(id_profesor=i+1, nombre=nombre, materia=materia)
            self.profesores.append(profesor)

        print("Profesores registrados correctamente.\n")

    def ingresar_notas(self):
        print("=== INGRESO DE NOTAS POR PROFESOR ===")
        for est in self.estudiantes:
            print(f"Ingresando notas para: {est.nombre}")
            num_notas = int(input("¿Cuántas notas desea agregar?: "))

            for n in range(num_notas):
                nota = float(input(f"Nota {n+1}: "))
                est.agregar_nota(nota)

        print("Notas ingresadas correctamente\n")

    def mostrar_resultados(self):
        print("=== RESULTADOS FINALES ===")

        for est in self.estudiantes:
            print(f"ID: {est.id}")
            print(f"Nombre: {est.nombre}")
            print(f"Notas: {est.notas}")
            print(f"Promedio: {est.promedio():.2f}")
            print(f"Estado: {est.estado()}")
            print("-" * 30)

        print("\n=== PROFESORES REGISTRADOS ===")
        for prof in self.profesores:
            print(f"ID: {prof.id}")
            print(f"Profesor: {prof.nombre}")
            print(f"Materia: {prof.materia}")
            print("-" * 30)
