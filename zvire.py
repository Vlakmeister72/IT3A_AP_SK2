import random

class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto

        pass
    
    def zvuk(self):
        return "???"
    
    def predstav_se(self):
        return f"Jsem {self.jmeno} a je mi {self.vek}."
        pass

    def kde_jsi(self):
        return f"Jsem v místě zvaném {self.misto}."
    
    def jdi_na(self, n_misto:str):
        self.misto = n_misto
        return f"Přesunul jsem se na {n_misto}"
       




zvire = Zvire("Šoral", 50)
print(zvire.predstav_se())
print(zvire.kde_jsi())
print(zvire.jdi_na("Kadeřnictví"))
print(zvire.kde_jsi())

zvire2 = Zvire("Wolfram", 32, "PentHouse")
print(zvire2.predstav_se())
print(zvire2.kde_jsi())
print(zvire.jdi_na("Klokánek"))
print(zvire.kde_jsi())

class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno

        pass

    def zvuk(self):
        return "[zmatená kachna z partičky]"
    
    def aport(self):
        return f"{self.jmeno} přinesl granát!"
    
    def vycesat(self):
        if (random.randint(0,1) > 0):
            return f"{self.jmeno} utekl před tvým kartáčem"
        else:
            return f"{self.jmeno} se nechal vyčesat"
        
    def predstav_se(self):
        return f"{super().predstav_se()} jsem {self.plemeno}."

radegast = Pes("Radegast", 2, "undefined", "gauč")
print(radegast.predstav_se())
print(radegast.kde_jsi())
print(radegast.zvuk())
print(radegast.aport())
print(radegast.vycesat())
print("-" * 20)

class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.barva = barva

        pass

    def predstav_se(self):
        return f"{super().predstav_se()} jsem {self.barva}."

    def hrani(self):
        if (random.randint(0,1) > 0):
            return f"{self.jmeno} ti škrábl a utekl"
        else:
            return f"{self.jmeno} se nechal a vrní"
    
    def zvuk(self):
        return "meow meow nibba"
    
bingus = Kocka("Bingus", 3, "žůžová", "gauč")
print(bingus.predstav_se())
print(bingus.kde_jsi())
print(bingus.zvuk())
print(bingus.hrani())

class Had(Zvire):
    def __init__(self, jmeno, vek, delka:int, jedovaty:bool, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.delka = delka
        self.jedovaty = jedovaty
    
    def zvuk(self):
        return "i can ssssssuck ur blood"
    
    def predstav_se(self):
        if self.jedovaty:
            typ = "jedovatý"
        else:
            typ = "škrtič"
        return f"Jsem {self.jmeno}, měřím {self.delka} cm a jsem {typ}."

voraisha = Had("Voraisha", 27, 500, False)
print(voraisha.predstav_se())        

zoo = [radegast, bingus, voraisha]

for obyvatel in zoo:
    print(obyvatel.predstav_se())
    print(obyvatel.zvuk())
    print("-" * 20)



