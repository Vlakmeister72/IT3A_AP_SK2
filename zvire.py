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