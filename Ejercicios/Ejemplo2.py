class Humano():
    nombre = ""
    edad = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        # Aquí pueden ir más cosas que se hacen en un constructor

    def presentarse(self):
        print("Hola a todos Me llamo {} y mi edad actual es {}".format(
            self.nombre, self.edad))


h = Humano("Jhoel", 21)
h.presentarse()
h2 = Humano("Jose", 18)
h2.presentarse()