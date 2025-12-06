class Estudiante:
    def __init__(self, id_estudiante, nombre):
        self.id = id_estudiante
        self.nombre = nombre
        self.notas = []   

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def estado(self):
        return "APROBADO" if self.promedio() >= 3.0 else "REPROBADO"
