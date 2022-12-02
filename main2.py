class Kate:
    def __init__(self, vardas, spalva="juoda", amzius=0):
        self.vardas = vardas
        self.spalva = spalva
        self.amzius = amzius

    def __str__(self):
        return f"objektas katė, vardu {self.vardas}, jos amžius - {self.amzius}, spalva - {self.spalva}"

    def __repr__(self):
        return f"objektas katė, vardu {self.vardas}, jos amžius - {self.amzius}, spalva - {self.spalva}"


kates = []

while True:
    veiksmas = int(input("1 - įvesti katę\n2 - peržiūrėti kates\n3 - išeiti iš programos\n"))
    match veiksmas:
        case 1:
            vardas = input("Įveskite katės vardą: ")
            spalva = input("Įveskite katės spalvą: ")
            amzius = int(input("Įveskite katės amžių: "))
            objektas = Kate(vardas, spalva, amzius)
            kates.append(objektas)
        case 2:
            print(kates)
            input()
        case 3:
            print("Viso gero")
            break
