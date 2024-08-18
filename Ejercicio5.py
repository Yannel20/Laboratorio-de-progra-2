 #Ejercicio 5 - Tienda de Videojuegos
# Una tienda de videojuegos vende títulos populares (nuevos o usados).
# Todos los productos son de la marca GameMaster, una marca líder en la industria.
# Se requiere almacenar sus 5 principales características.
# Todos los juegos son importados y su precio de venta es igual al precio de compra multiplicado por 1.3, lo que corresponde a su margen de ganancia.

class TiendaVideojuegos:
    EstadoJuego = ""  # Nuevo o Usado
    TituloJuego = ""
    Cantidad = 0
    PrecioCosto = 0
    PrecioVenta = 0

    def _init_(self):
        self.PrecioCosto = 0
        self.PrecioVenta = 0
        self.Cantidad = 0

    # Aquí redondeo para evitar que aparezcan muchos decimales
    def Cobro(self):
        self.PrecioVenta = round((self.Cantidad * self.PrecioCosto) * 1.3, 2)
        print(f"Precio a Cobrar: ${self.PrecioVenta}")

    def DatosCompra(self):
        self.Cobro()

    # Aquí es donde el usuario ingresa los datos de la compra  
    def RegistrarCompra(self):
        print("** Bienvenido a GameMaster Store **")
        self.EstadoJuego = input("¿El juego es Nuevo o Usado? (N/U): ").lower()
        self.TituloJuego = input("Título del juego: ")
        self.Cantidad = int(input(f"¿Cuántas copias de {self.TituloJuego} llevarás?: "))
        self.PrecioCosto = float(input("Precio de Compra del Proveedor: $"))
        print("***************")

    def MostrarDatosCompras(self):
        print("** Detalles de la Compra **")
        if self.EstadoJuego == "n":
            print("Este es un juego nuevo.")
        elif self.EstadoJuego == "u":
            print("Este es un juego usado.")
        print("****************")
        print(f"Título del Juego: {self.TituloJuego}")
        print(f"Cantidad: {self.Cantidad}")
        self.DatosCompra()

# Creación de una instancia de TiendaVideojuegos
Compra1 = TiendaVideojuegos()
print("**** Bienvenido al sistema ****")
Compra1.RegistrarCompra()
Compra1.MostrarDatosCompras()
print("***************")