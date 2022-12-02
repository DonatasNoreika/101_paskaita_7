class Gyvunas:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print("Bėgu")

class Kate(Gyvunas):
    def miaukseti(self):
        print("Miau")

    def begti(self):
        print("Sėlinu")

class Suo(Gyvunas):
    def loti(self):
        print("Au")


vezlys = Gyvunas("Tadas", "rudas")
kate1 = Kate("Mūza", "Pilka")
suo1 = Suo("Čakas", "Baltas")

vezlys.begti()
kate1.begti()
kate1.miaukseti()
suo1.begti()
suo1.loti()

