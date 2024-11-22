class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def reservar(self):
        if not self.disponible:
            print(f"La habitación {self.numero} ya está reservada.")
        else:
            self.disponible = False
            print(f"Habitación {self.numero} reservada exitosamente.")

    def liberar(self):
        if self.disponible:
            print(f"La habitación {self.numero} ya está disponible.")
        else:
            self.disponible = True
            print(f"Habitación {self.numero} liberada exitosamente.")

    def mostrar_informacion(self):
        print(f"Habitación {self.numero}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio por noche: ${self.precio:.2f}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")



if __name__ == "__main__":
    habitacion1 = Habitacion(101, "Simple", 75.00)
    habitacion2 = Habitacion(102, "Suite", 150.00, disponible=False)

    print("\nDetalles de la habitación 1:")
    habitacion1.mostrar_informacion()

    print("\nDetalles de la habitación 2:")
    habitacion2.mostrar_informacion()

    print("\nIntentando reservar la habitación 1:")
    habitacion1.reservar()

    print("\nIntentando reservar la habitación 2:")
    habitacion2.reservar()

    print("\nLiberando la habitación 2:")
    habitacion2.liberar()

    print("\nDetalles actualizados de la habitación 2:")
    habitacion2.mostrar_informacion()
