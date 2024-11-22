class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            print("El precio no puede ser negativo.")
        else:
            self.precio = nuevo_precio
            print(f"El nuevo precio de {self.nombre} es ${self.precio:.2f}.")

    def ajustar_inventario(self, cantidad_cambio):
        nueva_cantidad = self.cantidad + cantidad_cambio
        if nueva_cantidad < 0:
            print(f"No se puede ajustar el inventario. Cantidad disponible insuficiente.")
        else:
            self.cantidad = nueva_cantidad
            print(f"La nueva cantidad de {self.nombre} en inventario es {self.cantidad} unidades.")

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad en inventario: {self.cantidad} unidades")



if __name__ == "__main__":
    producto = Producto("Laptop", 1200.00, 10)

    print("\nInformación del producto:")
    producto.mostrar_informacion()

    print("\nActualizando precio del producto:")
    producto.actualizar_precio(1300.00)

    print("\nAjustando inventario:")
    producto.ajustar_inventario(-3)  # Reduce el inventario en 3 unidades

    print("\nInformación actualizada del producto:")
    producto.mostrar_informacion()
