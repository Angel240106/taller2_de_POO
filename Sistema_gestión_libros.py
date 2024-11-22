class Libro:
    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        descuento = (self.precio * porcentaje) / 100
        self.precio -= descuento
        print(f"El precio después de aplicar el descuento de {porcentaje}% es: ${self.precio:.2f}")

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Precio: ${self.precio:.2f}")

    def es_mas_caro_que(self, otro_libro):
        if self.precio > otro_libro.precio:
            return self
        else:
            return otro_libro



if __name__ == "__main__":

    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico", 20.00)
    libro2 = Libro("1984", "George Orwell", "Distopía", 15.00)

    print("\nInformación del libro 1:")
    libro1.mostrar_informacion()

    print("\nInformación del libro 2:")
    libro2.mostrar_informacion()


    print("\nAplicando descuento al libro 1:")
    libro1.aplicar_descuento(10)


    libro_mas_caro = libro1.es_mas_caro_que(libro2)
    print("\nEl libro más caro es:")
    libro_mas_caro.mostrar_informacion()

