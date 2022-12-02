
class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(f"Automobilis {self.modelis}, metai - {self.metai}, kuro tipas - {self.kuro_tipas}")

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")

class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja pats")


audi_a7 = Automobilis(2022, "Audi A7", "benzinas")
audi_etron_gt = Elektromobilis(2022, "Audi E-Tron GT", "elektra")

audi_a7.vaziuoti()
audi_a7.stoveti()
audi_a7.pildyti_degalu()
audi_etron_gt.vaziuoti()
audi_etron_gt.stoveti()
audi_etron_gt.pildyti_degalu()
audi_etron_gt.vaziuoti_autonomiskai()