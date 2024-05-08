from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)
        self.agyak = 1


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam,ar):
        super().__init__(szobaszam, ar)
        self.agyak = 2

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)
    def add_foglalas(self, szobaszam, datum):
        self.foglalasok.append(Foglalas(szobaszam, datum))
        print(f"{szobaszam} szoba lefoglalva Ár: {self.arszobaszamalapjan(szobaszam)}")
    def arszobaszamalapjan(self, szobaszam):
        keresettar=0
        for szoba in self.szobak:
            if szoba.szobaszam==szobaszam:
                keresettar=szoba.ar
        return keresettar
    def foglalaslistazas(self):
        print("Foglalások")
        n=1
        for foglalas in self.foglalasok:
            print(f"{n}. Szobaszám: {foglalas.szobaszam} Dátum: {foglalas.datum}")
            n+=1

    def lehetfoglalni(self, szobaszam, datum):

        foglalhato=True
        for foglalas in self.foglalasok:
            if foglalas.szobaszam==szobaszam and foglalas.datum==datum:
                foglalhato=False
                print(f"Erre az időpontra a {szobaszam} számú szoba már nem foglalható")
        if datum<=datetime.today():
            foglalhato=False
            print(f"Hiba! Dátum múltbeli nem lehet ({datum})")
        vanilyenszoba = False
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                vanilyenszoba = True
        if vanilyenszoba==False:
            foglalhato=False
            print(f"Nincs ilyen szoba: {szobaszam}")
        return foglalhato

class Foglalas:
    def __init__(self, szobaszam, datum):
        self.szobaszam = szobaszam
        self.datum = datum

szalloda = Szalloda("Szálloda")
print(szalloda.nev)
szalloda.add_szoba(EgyagyasSzoba("101",15000))
szalloda.add_szoba(KetagyasSzoba("201", 20000))
szalloda.add_szoba(KetagyasSzoba("202",20010))
print("Szálloda szobái:")
for szoba in szalloda.szobak:
    print(f"szobaszám: {szoba.szobaszam} ár: {szoba.ar}")

szalloda.add_foglalas("101",datetime(2024, 5, 10))
szalloda.add_foglalas("201",datetime(2024, 6, 11))
szalloda.add_foglalas("201",datetime(2024, 6, 10))
szalloda.add_foglalas("202",datetime(2024, 7, 1))
szalloda.add_foglalas("202",datetime(2024, 7, 17))

szalloda.foglalaslistazas()

# felhasználói interfész
print("Üdvözlöm a szállodában")
while True:
    print("\nVálasszon egy műveletet:")
    print("1. Szoba foglalás")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("0. Kilépés")
    valasztas = input("Választás: ")
    if valasztas == "1":
        szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
        datum = input("Adja meg a foglalni kívánt dátumot (ÉÉÉÉ-HH-NN formátumban): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("A foglalás dátuma nem megfelelő")
            elif szalloda.lehetfoglalni(szobaszam,datum):
                szalloda.add_foglalas(szobaszam,datum)
        except ValueError:
            print("Hibás dátum formátum!")
    elif valasztas == "2":
        a=0
    elif valasztas == "3":
        szalloda.foglalaslistazas()
    elif valasztas == "0":
        print("Kilépés...")
        break
    else:
        print("Érvénytelen választás.")