class Vehiculos():
    Fabricante = ""
    ModeloVehiculo = ""
    AñoFabricacion = 0
    ColorVehiculo = ""
    TipoVehiculo = ""
    NumeroVin = ""
    NumeroMotor = ""
    CostoVehiculo = 0
    PrecioVentaVehiculo = 0
    NumeroAsientos = 0
    NumeroRuedas = 0

    # Constructor
    def _init_(self):
        self.CostoVehiculo = 0
        self.PrecioVentaVehiculo = 0
        self.NumeroMotor = ""
        self.AñoFabricacion = 0
        self.NumeroAsientos = 0
        self.NumeroRuedas = 0

    # Información del vehículo
    def InfoVehiculo(self):
        self.PrecioVentaVehiculo = self.CostoVehiculo * 1.4
        print(f"El vehículo fue adquirido a: ${self.CostoVehiculo}")
        print(f"El vehículo se vende a: ${self.PrecioVentaVehiculo}")

    # Registro de datos del vehículo
    def RegistrarVehiculo(self):
        print("Hola, bienvenido al Concesionario de Marine Ford")
        self.Fabricante = input("Fabricante del vehículo: ")
        self.ModeloVehiculo = input("Modelo del vehículo: ")
        self.AñoFabricacion = int(input("Año de fabricación del vehículo: "))
        self.ColorVehiculo = input("Color del vehículo: ")
        self.TipoVehiculo = input("Tipo de vehículo: ")
        self.NumeroVin = input("Número VIN: ")
        self.NumeroMotor = input("Número de Motor: ")
        self.NumeroAsientos = int(input("Cantidad de Asientos: "))
        self.NumeroRuedas = int(input("Cantidad de Ruedas: "))
        self.CostoVehiculo = int(input("Precio de Costo: $"))

    def AsignarDatosVehiculo(self, Fabricante, ModeloVehiculo, AñoFabricacion, ColorVehiculo, TipoVehiculo, NumeroVin, NumeroMotor, CostoVehiculo, PrecioVentaVehiculo, NumeroAsientos, NumeroRuedas):    
        self.Fabricante = Fabricante
        self.ModeloVehiculo = ModeloVehiculo
        self.AñoFabricacion = AñoFabricacion
        self.ColorVehiculo = ColorVehiculo
        self.TipoVehiculo = TipoVehiculo
        self.NumeroVin = NumeroVin
        self.NumeroMotor = NumeroMotor
        self.CostoVehiculo = CostoVehiculo
        self.PrecioVentaVehiculo = PrecioVentaVehiculo
        self.NumeroAsientos = NumeroAsientos    
        self.NumeroRuedas = NumeroRuedas

    # Mostrar los datos del vehículo
    def MostrarDatosVehiculo(self):
        print("Gracias por comprar en nuestro concesionario :D")
        print("Fabricante del vehículo: ", self.Fabricante)
        print("Modelo del vehículo: ", self.ModeloVehiculo)
        print("Año de fabricación del vehículo: ", self.AñoFabricacion)
        print("Color del vehículo: ", self.ColorVehiculo)
        print("Tipo de vehículo: ", self.TipoVehiculo)
        print("Número VIN: ", self.NumeroVin)
        print("Número de Motor: ", self.NumeroMotor)
        print("Cantidad de Asientos: ", self.NumeroAsientos)
        print("Cantidad de Ruedas: ", self.NumeroRuedas)
        self.InfoVehiculo()

# Creación de una instancia de Vehiculos
Vehiculo1 = Vehiculos()
print("*******************")
Vehiculo1.RegistrarVehiculo()
print("********************")
Vehiculo1.MostrarDatosVehiculo()