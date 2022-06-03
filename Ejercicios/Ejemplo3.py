class Moto:
    kilometraje=0
    modelo = 0
    marca = ""
    placa = ""
    def __init__(self,placa,marca,modelo,kilometraje):
       self.kilometraje = kilometraje
       self.modelo = modelo
       self.marca = marca
       self.placa = placa
       ## Metodos
    def Placa(self):
        return self.placa
    def Marca(self):
        return self.marca
    def Modelo(self):
        return self.modelo
    def Kilometraje(self):
        return self.kilometraje
    def MostrarDatos(self):
        print("Placa: " +self.Placa()+"\nMarca: "+self.Marca()+"\nModelo: "+self.Modelo()+"\nKilometraje: "+self.Kilometraje())

placa = input("Porfavor ingresar La Placa de la moto\n")
marca = input("Porfavor ingresar La Marca de la moto\n")
modelo = input("Porfavor ingresar El Modelo de la moto\n")
kilometraje = input("Porfavor ingresar el kilometraje\n")
Moto = Moto(placa,marca,modelo,kilometraje)
Moto.MostrarDatos()


