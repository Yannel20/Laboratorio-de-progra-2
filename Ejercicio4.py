class Inventario():
    CategoriaProducto = ""
    ModeloProducto = ""
    CapacidadAlmacenamiento = 0
    MemoriaRAM = 0
    PrecioProveedor = 0
    PrecioVentaFinal = 0

    # Constructor
    def _init_(self):
        self.PrecioProveedor = 0
        self.PrecioVentaFinal = 0
        self.CapacidadAlmacenamiento = 0
        self.MemoriaRAM = 0

    # Información del producto
    def InformacionProducto(self):
        self.PrecioVentaFinal = self.PrecioProveedor * 1.7
        print(f"El artículo fue adquirido a: ${self.PrecioProveedor}")
        print(f"El artículo se venderá a: ${self.PrecioVentaFinal}")

    # Registro de datos del producto
    def RegistrarProducto(self):
        print("Hola, bienvenido a Inventario")
        self.CategoriaProducto = input("Categoría de Producto: ")
        self.ModeloProducto = input("Modelo del Producto: ")
        self.CapacidadAlmacenamiento = int(input("Capacidad de Almacenamiento (en GB): "))
        self.MemoriaRAM = int(input("Memoria RAM (en GB): "))
        self.PrecioProveedor = int(input("Precio del Proveedor: $"))

    def AsignarDatosProducto(self, PrecioProveedor, PrecioVentaFinal, CategoriaProducto, ModeloProducto, CapacidadAlmacenamiento, MemoriaRAM):    
        self.CategoriaProducto = CategoriaProducto
        self.ModeloProducto = ModeloProducto
        self.CapacidadAlmacenamiento = CapacidadAlmacenamiento
        self.MemoriaRAM = MemoriaRAM
        self.PrecioProveedor = PrecioProveedor
        self.PrecioVentaFinal = PrecioVentaFinal

    # Mostrar los datos del producto
    def MostrarDatosProducto(self):
        print("Gracias por comprar en Inventario :D")
        print("Categoría de Producto: ", self.CategoriaProducto)
        print(f"Modelo del {self.CategoriaProducto}: ", self.ModeloProducto)
        print("Capacidad de Almacenamiento: ", self.CapacidadAlmacenamiento, " GB")
        print("Memoria RAM: ", self.MemoriaRAM, " GB")
        self.InformacionProducto()

# Creación de una instancia de Inventario
Producto1 = Inventario()
print("********Factura*********")
Producto1.RegistrarProducto()
print("********************")
Producto1.MostrarDatosProducto()