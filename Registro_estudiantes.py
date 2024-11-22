class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = []

    def inscribir_materia(self, materia):
        if materia in self.materias:
            print(f"La materia '{materia}' ya está inscrita.")
        else:
            self.materias.append(materia)
            print(f"Materia '{materia}' inscrita exitosamente.")

    def mostrar_materias(self):
        if self.materias:
            print(f"Materias inscritas de {self.nombre}:")
            for materia in self.materias:
                print(f"- {materia}")
        else:
            print(f"{self.nombre} aún no ha inscrito ninguna materia.")

    def actualizar_grado(self, nuevo_grado):
        self.grado = nuevo_grado
        print(f"El grado de {self.nombre} ha sido actualizado a {self.grado}.")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Grado: {self.grado}")
        self.mostrar_materias()



if __name__ == "__main__":
    estudiante = Estudiante("Luis Pérez", 14, "8vo grado")

    print("\nInformación del estudiante:")
    estudiante.mostrar_informacion()

    print("\nInscribiendo materias:")
    estudiante.inscribir_materia("Matemáticas")
    estudiante.inscribir_materia("Historia")
    estudiante.inscribir_materia("Matemáticas")  # Intentar inscribir la misma materia de nuevo

    print("\nMostrando materias:")
    estudiante.mostrar_materias()

    print("\nActualizando grado:")
    estudiante.actualizar_grado("9no grado")

    print("\nInformación actualizada del estudiante:")
    estudiante.mostrar_informacion()
