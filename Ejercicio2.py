class Tienda():
    ProductoA = ""
    ProductoB = ""
    CantidadProductoA = 0
    CantidadProductoB = 0
    PrecioProductoA = 0
    PrecioProductoB = 0
    TotalGanancia = 0
    ComprarProductoA = ""
    ComprarProductoB = ""

    def _init_(self):
        self.TotalGanancia = 0
        self.ProductoA = ""
        self.ProductoB = ""
        
    def TipoProductoA(self):
        if self.ProductoA == "opcion1":
            self.PrecioProductoA = (self.CantidadProductoA * 3.50) * 1.30
            print(f"Llevas {self.CantidadProductoA} unidades de ProductoA opción 1 y su precio es {self.PrecioProductoA}")
            print("Marca X")
        elif self.ProductoA == "opcion2":
            self.PrecioProductoA = (self.CantidadProductoA * 1.75) * 1.30
            print(f"Llevas {self.CantidadProductoA} unidades de ProductoA opción 2 y su precio es {self.PrecioProductoA}")
            print("Marca X")
        else:
            print("No conozco esa opción")

    def TipoProductoB(self):
        if self.ProductoB == "opcion1":
            self.PrecioProductoB = (self.CantidadProductoB * 0.25) * 1.30
            print(f"Llevas {self.CantidadProductoB} unidades de ProductoB opción 1 y su precio es {self.PrecioProductoB}")
            print("Marca Y")
        elif self.ProductoB == "opcion2":
            self.PrecioProductoB = round(((self.CantidadProductoB * 0.50) * 1.30),2)
            print(f"Llevas {self.CantidadProductoB} unidades de ProductoB opción 2 y su precio es {self.PrecioProductoB}")
            print("Marca Y")
        else:
            print("No conozco esa opción")

    def DetallesCompra(self):
        self.TipoProductoA()
        self.TipoProductoB()
        
    def RegistrarCompra(self):
        print("******************")
        self.ComprarProductoA = input("¿Llevarás ProductoA? (S/N): ").lower()
        if self.ComprarProductoA == "s":
            self.ProductoA = input("Tipo de ProductoA (opcion1/opcion2): ").lower()
            self.CantidadProductoA = int(input("¿Cuántas unidades de ProductoA llevas?: "))
        else: 
            print("Recuerda, tenemos producto exclusivo en ProductoA.")
        print("****************")   
        self.ComprarProductoB = input("¿Llevarás ProductoB? (S/N): ").lower()
        if self.ComprarProductoB == "s":
            self.ProductoB = input("Tipo de ProductoB (opcion1/opcion2): ").lower()
            self.CantidadProductoB = int(input("¿Cuántas unidades de ProductoB llevas?: "))
        else: 
            print("Recuerda, tenemos producto exclusivo en ProductoB.")
        print("****************")   

    def MostrarDetallesCompra(self):
        print("****************")
        print("Estado ProductoA: ", self.ComprarProductoA)
        if self.ComprarProductoA == "s":
            self.TipoProductoA()
        else: 
            print("Recuerda, tenemos producto exclusivo en ProductoA.")
        print("****************")
        print("Estado ProductoB: ", self.ComprarProductoB)
        if self.ComprarProductoB == "s":
           self.TipoProductoB()
        else: 
            print("Recuerda, tenemos producto exclusivo en ProductoB.")
        print("***************")

# Creación de una instancia de Tienda
Compra1 = Tienda()
print("*******************")
Compra1.RegistrarCompra()
print("********************")
Compra1.MostrarDetallesCompra()
print("********************")