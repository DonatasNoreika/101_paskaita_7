

class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def mazosiomis(self):
        return self.tekstas.lower()

    def gauti_zodi(self, eiles_nr):
        pass

sakinys1 = Sakinys("Code Academy")

print(sakinys1.atbulai())
print(sakinys1.mazosiomis())
print(sakinys1.gauti_zodi(2))

print(sakinys1)