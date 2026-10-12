class ChytreZarizeni:
    def __init__(self, nazev:str, mistnost:str, zapnuto:bool = False):
        self.nazev = nazev
        self.mistnost = mistnost
        self.zapnuto = zapnuto
        pass

    def predstav_se(self):
        return f"Jsem {self.nazev}, jsem v místnosti s názvem {self.mistnost}."

    def prepni_stav(self):
        if self.zapnuto == True:
            self.zapnuto = False
            return "Zařízení se vypnulo."
        else:
            self.zapnuto = True
            return "Zařízení se zapnulo."
    
    def proved_akci(self):
        return "Zařízení čeká na příkaz..."
    
class ChytraZarovka(ChytreZarizeni):
    def __init__(self, nazev, mistnost, zapnuto = False, barva:str = "Bílá"):
        super().__init__(nazev, mistnost, zapnuto)
        self.barva = barva

    def proved_akci(self):
        if self.zapnuto == True:
            return f"Svítí {self.barva} barva."
        else:
            return "Je zhasnuto."
    
    def zmen_barvu(self):
        self.barva = "Červená"
        return f"Změnil jsem barvu na {self.barva}."
    
NBION = ChytraZarovka("Niceboy ION SmartBulb RGB E27 12W", "Osobní Pokoj")
print(NBION.predstav_se())
print(NBION.prepni_stav())
print(NBION.proved_akci())
print(NBION.zmen_barvu())

class ChytraZasuvka(ChytreZarizeni):
    def __init__(self, nazev, mistnost, aktualni_odber_w:int, zapnuto = False):
        super().__init__(nazev, mistnost, zapnuto)
        self.aktualni_odber_w = aktualni_odber_w

    def proved_akci(self):
        if self.zapnuto == True:
            return f"Propouštím proud. Aktuální odběr:{self.aktualni_odber_w} W."
        else:
            return "Jsem vypnutý."
        
tptapo = ChytraZasuvka("TP-LINK Tapo P115", "Obývací pokoj", 120)
print(tptapo.predstav_se())
print(tptapo.prepni_stav())
print(tptapo.proved_akci())