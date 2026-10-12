class SitoveZarizeni:
    def __init__(self, nazev:str, ip_adresa:str, online:bool = False):
        self.nazev = nazev
        self.ip_adresa = ip_adresa
        self.online = online
        pass

    def zmena_stavu(self):
        if self.online == True:
            self.online = False
            return "Server je Offline."
        else:
            self.online = True
            return "Server je Online."
        
    def diagnostika(self):
        return f"Spouštím obecnou diagnostiku zařízení... Jsem {self.nazev}, moje adresa je {self.ip_adresa}."
    
class Router(SitoveZarizeni):
    def __init__(self, nazev: str, ip_adresa: str, pocet_portu:int, online: bool = False):
        super().__init__(nazev, ip_adresa, online)
        self.pocet_portu = pocet_portu

    def diagnostika(self):
        return f"{super().diagnostika()} Kontroluji LAN porty... Mám {self.pocet_portu} LAN portů."
    
    def restartuj_wifi(self):
        return "Restartování WiFi..."
    
bindus = Router("ASUS ROG Rapture GT-BE98, WiFi 7, AiMesh", "10.0.0.1", 7)
print(bindus.diagnostika())
print(bindus.restartuj_wifi())
    
class Server(SitoveZarizeni):
    def __init__(self, nazev, ip_adresa, os, online = False,):
        super().__init__(nazev, ip_adresa, online)
        self.os = os

    def operacni_system(self):
        return f"Bežím na operačním systému {self.os}."
    
souepls = Server("Server1", "192.168.10.0", "Ubuntu")
print(souepls.diagnostika())
print(souepls.operacni_system())
    
=======
class SitoveZarizeni:
    def __init__(self, nazev:str, ip_adresa:str, online:bool = False):
        self.nazev = nazev
        self.ip_adresa = ip_adresa
        self.online = online
        pass

    def zmena_stavu(self):
        if self.online == True:
            self.online = False
            return "Server je Offline."
        else:
            self.online = True
            return "Server je Online."
        
    def diagnostika(self):
        return "Spouštím obecnou diagnostiku zařízení..."
    
class Router(SitoveZarizeni):
    def __init__(self, nazev: str, ip_adresa: str, pocet_portu:int, online: bool = False):
        super().__init__(nazev, ip_adresa, online)
        self.pocet_portu = pocet_portu

    def diagnostika(self):
        return f"{super().diagnostika()} Kontroluji LAN porty..."
    
    def restartuj_wifi(self):
        return "Restartování WiFi..."
>>>>>>> e6d58488fedcc95b13d428ab40e7e13227a8ee25
