from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
        self.foglalt = False

    @abstractmethod
    def leiras(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kenyelmi_fok):
        super().__init__(ar, szobaszam)
        self.kenyelmi_fok = kenyelmi_fok

    def leiras(self):
        return f"Egyágyas szoba {self.szobaszam} számmal, {self.kenyelmi_fok} kényelemmel."

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, erkely):
        super().__init__(ar, szobaszam)
        self.erkely = erkely

    def leiras(self):
        return f"Kétágyas szoba {self.szobaszam} számmal, erkéllyel: {self.erkely}."

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szoba, datum):
        if szoba.foglalt:
            print("A szoba már foglalt.")
            return
        if datum < datetime.now():
            print("A dátum nem lehet a múltban.")
            return
        foglalas = Foglalas(szoba, datum)
        self.foglalasok.append(foglalas)
        szoba.foglalt = True
        return szoba.ar

    def lemondas(self, foglalas):
        if foglalas not in self.foglalasok:
            print("A foglalás nem létezik.")
            return
        self.foglalasok.remove(foglalas)
        foglalas.szoba.foglalt = False

    def list_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Foglalás {foglalas.datum} dátumra, {foglalas.szoba.leiras()}.")

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

# Felhasználói Interfész Példa
def main():
    szalloda = Szalloda("Példa Szálloda")
    szoba1 = EgyagyasSzoba(200000, 101, kenyelmi_fok="Elit")
    szoba2 = KetagyasSzoba(150000, 102, erkely=True)
    szoba3 = EgyagyasSzoba(100000, 103, kenyelmi_fok="Standard")
    szalloda.add_szoba(szoba1)
    szalloda.add_szoba(szoba2)
    szalloda.add_szoba(szoba3)

    while True:
        print("\n1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válasszon egy műveletet: ")
        if valasztas == "1":
            szobaszam = int(input("Adja meg a szoba számát: "))
            datum = input("Adja meg a foglalás dátumát (Év-Hónap-Nap formátumban): ")
            datum = datetime.strptime(datum, "%Y-%m-%d")
            for szoba in szalloda.szobak:
                if szoba.szobaszam == szobaszam:
                    szalloda.foglalas(szoba, datum)
                    break
            else:
                print("Nincs ilyen szobaszám.")
        elif valasztas == "2":
            szobaszam = int(input("Adja meg a szoba számát: "))
            datum = input("Adja meg a foglalás dátumát (Év-Hónap-Nap formátumban): ")
            datum = datetime.strptime(datum, "%Y-%m-%d")
            for foglalas in szalloda.foglalasok:
                if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                    szalloda.lemondas(foglalas)
                    break
            else:
                print("Nincs ilyen foglalás.")
        elif valasztas == "3":
            szalloda.list_foglalasok()
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()