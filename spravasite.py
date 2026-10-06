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