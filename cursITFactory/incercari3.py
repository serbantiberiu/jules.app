'''
a. Recomandat (usor)
1. Revizualizeaza intalnirea 6 si ia notite in caz ca ti-a scapat ceva

b. Obligatorii (mediu)

Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei

1.Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()'''


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
        self.pi = 3.14

    def descrie_cerc(self):
        print(f'Cercul meu are raza', self.raza, ' cm si culoarea', self.culoare)

    def aria(self):
        return float(self.pi) * int(self.raza) ** 2

    def diametru(self):
        return int(self.raza) * 2

    def circumferinta(self):
        return int(self.raza) * float(self.pi) * 2


cerc1 = Cerc('50', 'turcoaz')
cerc1.descrie_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

'''2.Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele
Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().'''


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Dreptunghiul meu are lungimea de', self.lungime, 'cm ,latimea de', self.latime, ' cm si culoarea',
              self.culoare)

    def aria(self):
        return int(self.lungime) * int(self.latime)

    def perimetru(self):
        return int(self.lungime) * int(self.latime) * 2

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


dreptunghi1 = Dreptunghi('287', '5', 'turcoaz')
dreptunghi1.descrie_dreptunghi()
print(dreptunghi1.aria())
print(dreptunghi1.perimetru())
dreptunghi1.schimba_culoarea('roz')
dreptunghi1.descrie_dreptunghi()

'''3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)'''


class Angajat:
    # constructor
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    # metode
    def descrie(self):
        print(f'Ma numesc', self.nume, self.prenume, 'si am salariu de', self.salariu, 'euro.')

    def nume_complet(self):
        return self.nume + self.prenume

    def salariu_lunar(self):
        return int(self.salariu)

    def salariu_anual(self):
        return int(self.salariu) * 12

    def marire_salariu(self, procent):
        return int(self.salariu) + (int(self.salariu) * procent / 100)


angajat1 = Angajat('Popescu', 'Ion', '1000')
angajat1.descrie()
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
print(angajat1.marire_salariu(25))
'''4.
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)'''


class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul', self.titular_cont, ' are in contul', self.iban, ' suma de', self.sold, 'lei')

    def debitare_cont(self, suma):
        if self.sold >= suma:
            self.sold = int(self.sold) - int(suma)
            return self.sold
        else:
            return 'Fonduri insuficiente'

    def creditare_cont(self, suma):
        self.sold = int(self.sold) + int(suma)
        return self.sold


cont1 = Cont('RO10ING00000123456', 'Maria Ionescu', '1000')
cont1.afisare_sold()
print(cont1.debitare_cont('300'))
print(cont1.creditare_cont('35000'))

'''BONUS: (daca aveti timp si doriti sa lucrati suplimentar)
5.
Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total
Telefon |      7       |       700       | 49000

Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
'''

from datetime import datetime


class Factura():
    seria = 'FPP'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua
        return cantitate_noua

    def schimba_pretul(self, pret):
        self.pret_buc = pret
        return pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        return nume

    def genereaza_factura(self):
        print('Factura seria', self.seria, 'numar', self.numar)
        print('Data:', datetime.now())


factura1 = Factura('1', 'pixuri', '100', '1')
print(factura1.schimba_cantitatea('200'))
print(factura1.schimba_pretul('2'))
print(factura1.schimba_nume_produs('radiere'))
print('__________________________')
factura1.genereaza_factura()

'''6.
Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumita viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza'''



class Masina:
    culoare = 'gri'
    viteza_actuala = 0
    culori_disponibile = {'alb', 'negru', 'albastru', 'auriu', 'visiniu', 'verde'}
    marca = 'Range'
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def inmatriculare(self):
        self.inmatriculata = True
        print(self.inmatriculata)

    def vopseste(self, culoare_noua):
        if culoare_noua in self.culori_disponibile:
            self.culoare = culoare_noua
            print(self.culoare)
        else:
            print('Culoarea nu este disponibila')

    def accelereaza(self, viteza):
        self.viteza_actuala = viteza
        if int(viteza) < 0:
            print('Eroare')
        elif int(viteza) > int(self.viteza_maxima):
            self.viteza_actuala = self.viteza_maxima
            print(self.viteza_actuala)
        else:
            int(self.viteza_actuala) == int(viteza)
            print(self.viteza_actuala)

    def franare(self):
        self.viteza_actuala = 0
        print(self.viteza_actuala)


masina1 = Masina('80', '200')
masina1.descrie()
print('_______________')
masina1.inmatriculare()
masina1.vopseste('galben')
masina1.accelereaza('100')
print('_____________')
masina1.descrie()
masina1.franare()

'''7. Clasa TodoList

Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict'''

