class Hero:
    def __init__(self, jmeno:str, lvl:int, lokace:str = "SafeHouse"):
        self.jmeno = jmeno
        self.lvl = lvl
        self.lokace = lokace

        pass

    def pokrik(self):
        return "???"
    
    def predstav_se(self):
        return f"Jsem {self.jmeno} a mám Level {self.lvl}."
    
    def kde_jsi(self):
        return f"Jsem v lokaci zvaném {self.lokace}."
    
    def presun_se(self, n_lokace:str):
        self.lokace = n_lokace
        return f"Přesunul jsem se na {n_lokace}."
    
Lucia = Hero("Lucia Caminos", 21)
print(Lucia.pokrik())
print(Lucia.predstav_se())
print(Lucia.kde_jsi())
print(Lucia.presun_se("LTD Gas Station"))
print(Lucia.kde_jsi())


    