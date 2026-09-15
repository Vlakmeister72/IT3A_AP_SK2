class Robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str = "zničit lidstvo"):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol

        pass

    def zvuk(self):
        return "boop boop beep"
    
    def diagnostika(self):
        return f"Jsem {self.oznaceni}. Právě mám baterii na úrovni {self.baterie}%."
    
    def aktualni_ukol(self):
        return f"Mým úkolem je {self.ukol}."
    
    def zadej_ukol(self, n_ukol:str):
        self.ukol = n_ukol
        return f"Úkol se změnil: {n_ukol}."
    
Model101 = Robot("Model 101", 100)
print(Model101.zvuk())
print(Model101.diagnostika())
print(Model101.aktualni_ukol())
print(Model101.zadej_ukol("zachránit lidstvo"))
