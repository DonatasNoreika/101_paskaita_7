
class Kate:
    def __init__(self, vardas, spalva="juoda", amzius=0):
        self.vardas = vardas
        self.spalva = spalva
        self.amzius = amzius
        # print(f"Sukurta katė {self.vardas}")

    def miaukseti(self, zinute="Miau", kiekis=1):
        print(f"Katė {self.vardas} sako {zinute * kiekis}")

    def __str__(self):
        return f"objektas katė, vardu {self.vardas}, jos amžius - {self.amzius}, spalva - {self.spalva}"

kate1 = Kate("Mūza", "juoda", 14)
kate2 = Kate("Rokis", "balta", 3)

print(kate1)
print(kate2)