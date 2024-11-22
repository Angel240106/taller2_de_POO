class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def conducir(self, km):
        if km < 0:
            print("El kilometraje no puede disminuir.")
        else:
            self.kilometraje += km
            print(f"Has conducido {km} km. Kilometraje actual: {self.kilometraje} km.")

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Kilometraje: {self.kilometraje} km")

    def es_vehiculo_antiguo(self):
        from datetime import date
        año_actual = date.today().year
        return (año_actual - self.año) > 20



if __name__ == "__main__":
    mi_vehiculo = Vehiculo("Toyota", "Corolla", 1995, 200000)

    print("\nDetalles del vehículo:")
    mi_vehiculo.mostrar_detalles()

    print("\n¿Es vehículo antiguo?")
    if mi_vehiculo.es_vehiculo_antiguo():
        print("Sí, este vehículo tiene más de 20 años.")
    else:
        print("No, este vehículo tiene menos de 20 años.")

    print("\nConduciendo el vehículo:")
    mi_vehiculo.conducir(150)

    print("\nDetalles actualizados del vehículo:")
    mi_vehiculo.mostrar_detalles()
