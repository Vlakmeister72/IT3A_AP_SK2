import random

class Vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:int = 100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze

        pass

    def zvuk_motoru(self):
        return "???"
    
    def info(self):
        return f"Vozidlo {self.znacka}, rok {self.rok_vyroby}"
    
    def startuj(self):
        if self.stav_nadrze > 0:
            return f"{self.zvuk_motoru()} Vozidlo se nastartovalo."
        else:
            return "Došla šťáva, ty pizzo."

class Auto(Vozidlo):
    def __init__(self, znacka: str, rok_vyroby: int, typ_prevodovky:str, stav_nadrze: int = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_prevodovky
    
    def zvuk_motoru(self):
        return "Vrum vrum madafaka!"
    
    def zatrub(self):
        if (random.randint(0,1) > 0):
            return "drž hubu, nebudu troubit ty bidzo"
        else:
            return "awooga"
        
    def prevdovka(self):
        return f"Mám {self.typ_prevodovky} převodovku."
        
skoda_octavia = Auto("Škoda", 1998, "Manuální")
print(skoda_octavia.info())
print(skoda_octavia.prevdovka())
print(skoda_octavia.zatrub())
print(skoda_octavia.startuj())

class Lokomotiva(Vozidlo):
    def __init__(self, znacka: str, rok_vyroby: int, typ_paliva:str, uziti:str, stav_nadrze: int = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_paliva = typ_paliva
        self.uziti = uziti
    
    def palivo(self):
        if self.typ_paliva == "Pára":
            return "Jsem parní lokomotiva."
        elif self.typ_paliva == "Nafta":
            return "Jsem motorová lokomotiva"
        elif self.typ_paliva == "Elektřina":
            return "Jsem elektrická lokomotiva"
        
    def zvuk_motoru(self):
        if self.typ_paliva == "Pára":
            return "paf paf bidzo"
        elif self.typ_paliva == "Nafta":
            return "vrum vrum madafaka!"
        elif self.typ_paliva == "Elektřina":
            return "bzz bzz"
        
    def uzitka(self):
        return f"Jsem {self.uziti} lokomotiva."
    
velky_bejcek = Lokomotiva("Českomoravská-Kolben", 1924, "Pára", "Nákladní")
print(velky_bejcek.info())
print(velky_bejcek.palivo())
print(velky_bejcek.zvuk_motoru())
print(velky_bejcek.uzitka())

slovenska_strela = Lokomotiva("Závody Tatra", 1936, "Nafta", "Rychlíková")
print(slovenska_strela.info())
print(slovenska_strela.palivo())
print(slovenska_strela.zvuk_motoru())
print(slovenska_strela.uzitka())

bobina = Lokomotiva("Škodovy Závody", 1953, "Elektřina", "Univerzální")
print(bobina.info())
print(bobina.palivo())
print(bobina.zvuk_motoru())
print(bobina.uzitka())
        
    

    