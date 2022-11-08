from datetime import date
'''b. Obligatorii (mediu)

Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
'''
# Exercitiul 1 -----------------------------------------------

'''E1 - 1. Clasa Cerc;Atribute: raza, culoare;Constructor pt ambele atribute'
      'Metode:descrie_cerc() - va PRINTA culoarea si raza;aria() - va RETURNA aria diametru() circumferinta()'''


class Cerc:
    PI = 3.14

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul are raza {self.raza} si culoarea {self.culoare}')

    def aria(self):
        return self.PI * self.raza * self.raza

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return 2 * self.PI * self.raza


'''

2. 
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele
num
Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''


class Dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreprunghiul are lungimea {self.lungime}, latimea {self.latime}si culoarea {self.culoare}')

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * self.latime + 2 * self.lungime

    def schimba_culoare(self, culoare_noua):
        self.culoare = culoare_noua


'''
3.
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Ma numesc {self.nume} {self.prenume} si castig {self.salariu}')

    def nume_cumplet(self):
        print(f'Ma numesc {self.nume} {self.prenume}')

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return 12 * self.salariu

    def salariu_dupa_marire(self, procent):
        return self.salariu + (procent / 100) * self.salariu


'''
4.
Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate
Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''


class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}")

    def debitare_cont(self, suma):
        self.sold = self.sold - suma

    def creditare_cont(self, suma):
        self.sold = self.sold + suma


'''
BONUS: (daca aveti timp si doriti sa lucrati suplimentar)
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
class Factura:
    seria = "NNN"

    def __init__(self, numar, nume_produs, cantitate, pret_bucata):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_bucata

    def schimba_cantitate(self, cantitate_noua):
        self.cantitate = cantitate_noua

    def schimba_nume_produs(self, nume_nou):
        self.nume_produs = nume_nou

    def schimba_pret(self, pret_nou):
        self.pret_bucata = pret_nou

    def genereaza_factura(self):
        print(f"Factura seria {self.seria} numar {self.numar}")
        print(f'Data {date.today()}')
        print("Produs | Cantitate | Pret bucata | Total | Telefon")
        print(f"{self.nume_produs} | {self.cantitate} | {self.pret_bucata} | {self.pret_bucata * self.cantitate} ")


'''
6.
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
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''


class Masina:
    marca = "Mazda"
    viteza_actuala = 0
    culoare = "Gri"
    culori_disponibile = {"Rosu", "Gri", "Alb", "Negru", "Albastru"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f"Masina e  {self.marca} {self.model}, culoare {self.culoare}, "
              f"viteza actuala e {self.viteza_actuala}, viteza_maxima e {self.viteza_maxima} "
              f"si e inmatriculata {self.inmatriculata} ")

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            print(f"Culoare nu e in lista. Pueti alege doar {self.culori_disponibile}")

    def accelereaza(self, viteza):
        if viteza < 0:
            print("Viteza trebuie sa fie mai mare ca 0")
        elif viteza >= self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        self.viteza_actuala = 0


'''
7. Clasa TodoList

Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
'''


class ToDoList:
    dict = {}

    def adauga_task(self, nume, descriere):
        self.dict[nume] = descriere

    def finalizare_task(self, nume):
        try:
            self.dict.pop(nume)
        except KeyError as e:
            print(f"Taskul {nume} nu se afla in lista de to do")

    def afiseaza_todolist(self):
        print(f'Task-urile din TODO sunt: {self.dict.keys()}')

    def afiseaza_detalii_suplimentare(self, nume):
        if nume not in self.dict.keys():
            raspuns = input("vrei sa il adaugi in dict?")
            if raspuns.lower() == "da":
                detalii = input("da-mi detalii pt task")
                self.dict[nume] = detalii
            else:
                print("la revedere")
        else:
            print(f'Taskul {nume}, are ca descriere {self.dict.get(nume)}')