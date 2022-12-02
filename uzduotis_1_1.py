class Sakinys:
    def __init__(self, tekstas='Zen of Python'):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def mazosiomis(self):
        return self.tekstas.lower()

    def didziosiomis(self):
        return self.tekstas.upper()

    def gauti_zodi(self, eiles_nr):
        return self.tekstas.split()[eiles_nr - 1]

    def ieskoti(self, ieskomas):
        return self.tekstas.count(ieskomas)

    def pakeisti(self, senas, naujas):
        return self.tekstas.replace(senas, naujas)

    def info(self):
        zodziu_kiekis = len(self.tekstas.split())
        skaiciai = sum(i.isnumeric() for i in self.tekstas)
        didziosios = sum(i.isupper() for i in self.tekstas)
        mazosios = sum(i.islower() for i in self.tekstas)
        print(f"Žodžių kiekis: {zodziu_kiekis}, Skaičiai: {skaiciai}, Didžiosios: {didziosios}, Mažosios: {mazosios}")

    def __str__(self):
        return f"Tekstas: {self.tekstas}"


sakinys1 = Sakinys("Code Academy")

print(sakinys1.atbulai())
print(sakinys1.mazosiomis())
print(sakinys1.didziosiomis())
print(sakinys1.gauti_zodi(2))
print(sakinys1.ieskoti("Code"))
print(sakinys1.pakeisti("Code", "Music"))
sakinys1.info()
sakinys2 = Sakinys()
print(sakinys2.didziosiomis())
print(sakinys1)