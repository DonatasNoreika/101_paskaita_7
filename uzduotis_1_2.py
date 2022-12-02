import datetime

class Sukaktis:
    def __init__(self, data="2000-01-01 12:12:12"):
        self.data = datetime.datetime.strptime(data, "%Y-%m-%d %X")

    def kiek_praejo_laiko(self):
        skirtumas = datetime.datetime.today() - self.data
        print("Praėjo: ")
        print("Metų:", skirtumas.days // 365)
        print("Mėnesių:", skirtumas.days // 365 * 12)
        print("Dienų:", skirtumas.days)
        print("Valandų:", round(skirtumas.total_seconds() // 60 // 60))
        print("Minučių:", round(skirtumas.total_seconds() // 60))
        print("Sekundžių:", round(skirtumas.total_seconds()))

    def ar_keliamieji(self):
        metai = self.data.year
        return metai % 400 == 0 or (metai % 100 != 0 and metai % 4 == 0)

    def prideti_dienas(self, dienos):
        return self.data + datetime.timedelta(days=dienos)

    def atimti_dienas(self, dienos):
        return self.data - datetime.timedelta(days=dienos)

    def __str__(self):
        return (f"Data: {self.data}")

data1 = Sukaktis("2000-1-1 12:12:11")
data1.kiek_praejo_laiko()
print(data1.ar_keliamieji())
print(data1.prideti_dienas(5))
print(data1.atimti_dienas(5))


data2 = Sukaktis()
print(data1)
print(data2)
