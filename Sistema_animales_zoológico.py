class Animal:
    def __init__(self, nombre, especie, edad, habitat):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def cumplir_anos(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años.")

    def cambiar_habitat(self, nuevo_habitat):
        # Modifica el hábitat del animal
        self.habitat = nuevo_habitat
        print(f"{self.nombre} ahora vive en el hábitat de {self.habitat}.")

    def mostrar_detalles(self):
        # Muestra los detalles del animal
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")
        print(f"Hábitat: {self.habitat}")



if __name__ == "__main__":
    leon = Animal("Leo", "León", 5, "Sabana")
    tigre = Animal("Tigris", "Tigre", 3, "Selva tropical")

    print("\nDetalles del animal 1:")
    leon.mostrar_detalles()

    print("\nDetalles del animal 2:")
    tigre.mostrar_detalles()

    print("\nLeo cumple años:")
    leon.cumplir_anos()

    print("\nTigris cambia de hábitat:")
    tigre.cambiar_habitat("Reserva natural")

    print("\nDetalles actualizados del animal 1:")
    leon.mostrar_detalles()

    print("\nDetalles actualizados del animal 2:")
    tigre.mostrar_detalles()
