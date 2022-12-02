import pickle

class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma}, siuntėjas - {self.siuntejas}, info: {self.info}"

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, info):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        self.info = info

    def __str__(self):
        return f"Išlaidos: {self.suma}, atsiskaitymo būdas - {self.atsiskaitymo_budas}, įsigyta prekė/paslauga - {self.isigyta_preke_paslauga}, info: {self.info}"

class Biudzetas:
    def __init__(self):
        self.zurnalas = self.gauti_zurnala()

    def gauti_zurnala(self):
        try:
            with open("zurnalas.pkl", 'rb') as r_file:
                zurnalas = pickle.load(r_file)
        except:
            zurnalas = []
        return zurnalas

    def irasyti_zurnala(self, zurnalas):
        with open("zurnalas.pkl", 'wb') as w_file:
            pickle.dump(zurnalas, w_file)

    def prideti_pajamas(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala(self.zurnalas)
        
    def prideti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, info):
        irasas = PajamuIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala(self.zurnalas)

    def perziureti_zurnala(self):
        for irasas in self.zurnalas:
            print(irasas)

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            elif type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        print("Balansas:", suma)

biudzetas = Biudzetas()

while True:
    veiksmas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - peržiūrėti žurnalą\n4 - gauti balansą\n0 - išeiti iš programos\n"))
    if veiksmas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Įveskite siuntėją: ")
        info = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_pajamas(suma, siuntejas, info)
    if veiksmas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įveskite įsigytą prekę ar paslaugą: ")
        info = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
    if veiksmas == 3:
        biudzetas.perziureti_zurnala()
    if veiksmas == 4:
        biudzetas.gauti_balansa()
    if veiksmas == 0:
        print("Viso gero")
        break
