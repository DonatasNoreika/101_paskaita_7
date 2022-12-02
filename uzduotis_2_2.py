import datetime

class Darbuotojas:
    def __init__(self, vardas, ikainis, dirba_nuo):
        self.vardas = vardas
        self.ikainis = ikainis
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo,"%Y-%m-%d")

    def _nudirbo_dienu(self):
        return (datetime.datetime.today() - self.dirba_nuo).days

    def gauti_atlyginima(self):
        return self._nudirbo_dienu() * 8 * self.ikainis

class NormalusDarbuotojas(Darbuotojas):
    def _nudirbo_dienu(self):
        return (datetime.datetime.today() - self.dirba_nuo).days / 7 * 5


darbuotojas1 = Darbuotojas("Jotautas", 20, "2015-01-01")
print(darbuotojas1.gauti_atlyginima())
darbuotojas2 = NormalusDarbuotojas("Tomas", 20, "2015-01-01")
print(darbuotojas2.gauti_atlyginima())
