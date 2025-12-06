from sistema_notas import SistemaNotas

def main():
    sistema = SistemaNotas()

    sistema.registrar_estudiantes()
    sistema.registrar_profesores()
    sistema.ingresar_notas()
    sistema.mostrar_resultados()

if __name__ == "__main__":
    main()
