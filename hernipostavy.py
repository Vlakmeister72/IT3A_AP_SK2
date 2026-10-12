import random

class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi
        pass

    def predstav_se(self):
        return f"Jmenuji se {self.jmeno}, mám {self.zdravi} HP."
    
    def utok(self):
        return 0
    
vito = Postava("Vito Scaletta", 100)
print(vito.predstav_se())
print(vito.utok())

class Rytir(Postava):
    def __init__(self, jmeno, brneni:str, zdravi):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni

    def utok(self):
        dice = random.randint(10,20)
        return f"Utočil jsem se skórem {dice}."
    
    def zablokuj(self):
        return "Zablokoval jsem útok!"
    
    def co_mas_za_brneni(self):
        return f"Mám {self.brneni} brnění."
    
kris = Rytir("Kris Dreemurr", "Železné", 240)
print(kris.predstav_se())
print(kris.co_mas_za_brneni())
print(kris.utok())
print(kris.zablokuj())

class Mag(Postava):
    def __init__(self, jmeno, mana:int, zdravi):
        super().__init__(jmeno, zdravi)
        self.mana = mana

    def utok(self):
        dmg = random.randint(25,40)
        if self.mana >= 10:
            self.mana - 10
            return f"Útočil jsem s manou s {dmg} poškozením!"
        else: 
            return "Nemám manu! Útočil jsem pouze slabě holí s 5 poškozením."

ralsei = Mag("Ralsei", 45, 210)
print(ralsei.predstav_se())
print(ralsei.utok())

class Sup(Postava):
    def __init__(self, jmeno, TP:int, zdravi):
        super().__init__(jmeno, zdravi)
        self.TP = TP

    def utok(self):
        dmg = random.randint(100,365)
        if self.TP >= 50:
            self.TP - 50
            return f"Útočil/a jsem s Rude Busterem s {dmg} poškozením!"
        else:
            "Jseš debil? Nemám dost TP na to abych to použil/a!"

susie = Sup("Susie", 100, 290)
print(susie.predstav_se())
print(susie.utok())