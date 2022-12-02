class Tevas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde


class Vaikas(Tevas):
    def __init__(self, vardas, pavarde, mokykla):
        super().__init__(vardas, pavarde)
        self.mokykla = mokykla


tevas = Tevas("Rokas", "Budreika")
vaikas = Vaikas("Urtė", "Budreikaitė", "Čiurlionio")

print(vaikas.mokykla)