from datetime import date

print('Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei')
print('\n1. \
\nClasa Cerc\
\nAtribute: raza, culoare\
\nConstructor pt ambele atribute\
\nMetode:\
\ndescrie_cerc() - va PRINTA culoarea si raza\
\naria() - va RETURNA aria \
\ndiametru() \
\ncircumferinta()\
')
pi = 3.14159265359
class Cerc():
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
    def descrie_cer(self):
        print(f'\nCercul are culoarea {self.culoare} si raza {self.raza}')
    def aria(self):
        aria = pi * self.raza ** 2
        return aria
    def diametru(self):
        diametru = self.raza*2
        return diametru
    def circumferinta(self):
        circumferinta = 2*pi*self.raza
        return circumferinta

cerc1 = Cerc(2,'verde')
cerc1.descrie_cer()
print(f'Aria cercului este: {cerc1.aria()}')
print(f'Diametrul cercului este: {cerc1.diametru()}')
print(f'Circumferinta cercului este: {cerc1.circumferinta()}')
cerc2 = Cerc(3,'albastru')
cerc2.descrie_cer()
print(f'Aria cercului este: {cerc2.aria()}')
print(f'Diametrul cercului este: {cerc2.diametru()}')
print(f'Circumferinta cercului este: {cerc2.circumferinta()}')
print('---------------------------------------------------------------------------------------------')

print('2. \
\nClasa Dreptunghi\
\nAtribute: lungime, latime, culoare\
\nConstructor pt toate atributele\
\nMetode:\
\ndescrie()\
\naria()\
\nperimetrul()\
\nschimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.\
\nPuteti verifica schimbarea culorii prin apelarea metodei descrie().\
')

class Dreptunghi():
    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    def descrie(self):
        print(f'Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}.')
    def aria(self):
        aria = self.lungime * self.latime
        return aria
    def perimetru(self):
        perimetru = 2*(self.lungime + self.latime)
        return perimetru
    def schimba_culoare(self,culoare):
        self.culoare = culoare
print('')
dreptunghi1 = Dreptunghi(2,3,'verde')
dreptunghi1.descrie()
print(f'Aria dreptunghiului este: {dreptunghi1.aria()}')
print(f'Perimetrul dreptunghiului este: {dreptunghi1.perimetru()}')
dreptunghi1.schimba_culoare("rosu")
dreptunghi1.descrie()
print('')
dreptunghi2 = Dreptunghi(3,4,'albastru')
dreptunghi2.descrie()
print(f'Aria dreptunghiului este: {dreptunghi2.aria()}')
print(f'Perimetrul dreptunghiului este: {dreptunghi2.perimetru()}')
dreptunghi2.schimba_culoare("violet")
dreptunghi2.descrie()
print('---------------------------------------------------------------------------------------------')

print('3.\
\nClasa Angajat\
\nAtribute: nume, prenume, salariu\
\nConstructor pt toate atributele\
\nMetode:\
\ndescrie()\
\nnume_complet()\
\nsalariu_lunar()\
\nsalariu_anual()\
\nmarire_salariu(procent)\
')

class Angajat():
    def __init__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    def descrie(self):
        print(f'Angajatul {self.nume} {self.prenume} are salariul de {self.salariu}.')
    def nume_complet(self):
        nume_complet = self.nume + ' ' + self.prenume
        return nume_complet
    def salariu_lunar(self):
        salariu_lunar = self.salariu
        return salariu_lunar
    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        return salariu_anual
    def marire_salariu(self,procent):
        marire_salariu = self.salariu * procent/100
        print(f'Angajatul a solicitat o marire de salariu de {procent}%({marire_salariu}), noul salariu fiind {self.salariu + marire_salariu}')
print('')
angajat1 = Angajat('Chirieac','Ovidiu',6000)
angajat1.descrie()
print(f'Numele salariatului este: {angajat1.nume_complet()}')
print(f'Salariul lunar al salariatului este: {angajat1.salariu_lunar()}')
print(f'Salariul anual al salariatului este: {angajat1.salariu_anual()}')
angajat1.marire_salariu(10)
print('')
angajat2 = Angajat('Chirieac','Sergiu',5000)
angajat2.descrie()
print(f'Numele salariatului este: {angajat2.nume_complet()}')
print(f'Salariul lunar al salariatului este: {angajat2.salariu_lunar()}')
print(f'Salariul anual al salariatului este: {angajat2.salariu_anual()}')
angajat1.marire_salariu(20)
print('---------------------------------------------------------------------------------------------')

print('4.\
\nClasa Cont\
\nAtribute: iban, titular_cont, sold\
\nConstructor pentru toate\
\nMetode:\
\nafisare_sold() - Titularul x are in contul y suma de n lei\
\ndebitare_cont(suma)\
\ncreditare_cont(suma)\
')

class Cont():
    def __init__(self,iban,titular_cont,sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')
    def debitare_cont(self,suma):
        self.sold = self.sold - suma
        return suma
    def creditare_cont(self,suma):
        self.sold = self.sold + suma
        return suma
print('')
cont1 = Cont('RO53INGB0000999908907564','Sergiu',16000)
cont1.afisare_sold()
print(f'Contul {cont1.iban} a debitat suma de {cont1.debitare_cont(200)} lei. Soldul curent: {cont1.sold} lei')
print(f'Contul {cont1.iban} a creditat suma de {cont1.creditare_cont(400)} lei. Soldul curent: {cont1.sold} lei')
print('')
cont1 = Cont('RO53INGB0000999908907563','Ovidiu',26000)
cont1.afisare_sold()
print(f'Contul {cont1.iban} a debitat suma de {cont1.debitare_cont(300)} lei. Soldul curent: {cont1.sold} lei')
print(f'Contul {cont1.iban} a creditat suma de {cont1.creditare_cont(500)} lei. Soldul curent: {cont1.sold} lei')
print('---------------------------------------------------------------------------------------------')

print('5.\
\nClasa Factura\
\nAtribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc\
\nConstructor: toate atributele, fara serie\
\nMetode:\
\nschimba_cantitatea(cantitate)\
\nschimba_pretul(pret)\
\nschimba_nume_produs(nume)\
\ngenereaza_factura() - va printa tabelar daca reusiti\
\nFactura seria x numar y\
\nData: generati automat data de azi\
\nProdus | cantitate | pret bucata | Total \
\nTelefon |      7       |       700       | 49000\
\nIndiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/\
')
class Factura():
    serie = 'DEMO'
    def __init__(self,numar,nume_produs,cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
    def schimba_cantitatea(self,cantitate):
        self.cantitate = cantitate
    def schimba_pretul(self,pret):
        self.pret_buc = pret
    def schimba_nume_produs(self,nume):
        self.nume_produs = nume
    def genereaza_factura(self):
        table = [['Produs', 'Cantitate', 'Pret', 'Total'], [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate*self.pret_buc]]
        print(f'\nFactura seria {self.serie} numar {self.numar}'
              f'\nData: {date.today()}')
        for row in table:
            print('| {:10} | {:^9} | {:^4} | {:>5} |'.format(*row))

factura1 = Factura(1,'Mouse',1,100)
factura1.genereaza_factura()
factura1.schimba_cantitatea(2)
factura1.schimba_pretul(250)
factura1.schimba_nume_produs('Tastatura')
factura1.genereaza_factura()
factura2 = Factura(15,'Mazare',123,24)
factura2.genereaza_factura()
factura2.schimba_cantitatea(100)
factura2.schimba_pretul(23)
factura2.schimba_nume_produs('Fasole')
factura2.genereaza_factura()
print('---------------------------------------------------------------------------------------------')

print('6.\
\nClasa Masina\
\nAtribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)\
\nCuloare = gri - toate masinile cand ies din fabrica sunt gri\
\nViteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica\
\nCulori disponibile = alegeti voi 5-7 culori\
\nMarca = alegeti voi - fabrica produce o singura marca dar mai multe modele\
\nInmatriculata = False\
\nConstructor: model, viteza_maxima\
\nMetode:\
\ndescrie() (se vor printa toate atributele, inafara de culori_disponibile)\
\ninmatriculare() - va schimba atributul inmatriculata in True\
\nvopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare\
\naccelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima\
\nfraneaza() - masina se va opri si va avea viteza 0\
')
class Masina():
    culoare = 'gri'
    viteza_actuala = 0
    culori_disponibile = ('maro','verde','rosu','albastru','alb','negru')
    marca = 'Volkwagen'
    inmatriculata = False
    def __init__(self,model,viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
    def descrie(self):
        print(f'Masina cu marca {self.marca}, model {self.model} de culoare {self.culoare} are viteza actuala de {self.viteza_actuala} KM/H, viteza maxima de {self.viteza_maxima} KM/H este inmatriculata? {self.inmatriculata}')
    def inmatriculare(self):
        self.inmatriculata = True
    def vopseste(self,culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            return culoare == self.culori_disponibile
    def accelereaza(self,viteza):
        if viteza + self.viteza_actuala < 0:
            print('Eroare: Viteza mai mica decat 0')
        elif viteza + self.viteza_actuala > self.viteza_maxima:
            print('Eroare: Viteza mai mare decat viteza maxima')
        else:
            self.viteza_actuala = viteza + self.viteza_actuala
            return self.viteza_actuala
    def franeaza(self):
        self.viteza_actuala = 0

masina1 = Masina('Passat',240)
masina1.descrie()
masina1.inmatriculare()
masina1.vopseste('verde')
masina1.accelereaza(250)
masina1.franeaza()
masina2 = Masina('Golf',280)
masina2.descrie()
masina2.inmatriculare()
masina2.vopseste('negru')
masina2.accelereaza(100)
masina2.franeaza()
print('---------------------------------------------------------------------------------------------')

print('7. Clasa TodoList\
\n|Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)\
\nLa inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor\
\nMetode:\
\nadauga_task(nume, descriere) - se va adauga in dict\
\nfinalizeaza_task(nume) - se va sterge din dict\
\nafiseaza_todo_list() - doar cheile\
\nafiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare\
\ndaca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.\
\nDaca acesta raspunde nu - la revedere\
\ndaca raspunde da - il cerem detalii task si salvam nume+detalii in dict\
')

class ToDoList():
    dict = {}
    def adauga_task(self, nume,descriere):
        dict[nume] = descriere
    def finalizeaza(self,nume):
        dict.pop(nume)
    def afiseaza_todo_list(self):
        print(dict.keys())
    def afiseaza_detalii_suplimentare(self,nume):
        if nume in dict.keys():
            print(dict[nume])
        else:
            raspuns = input('Taskul nu exista in ToDo List, vreti sa fie adaugat in lista? [DA/NU]')
            if raspuns == 'DA':
                detalii = input('Completati detaliile task-ului nou: ')
                dict[nume] = detalii
            else:
                print('La revedere')

todolist1 = ToDoList()
todolist1.adauga_task('cumparaturi','lapte')
todolist1.afiseaza_todo_list()
todolist1.finalizeaza('cumparaturi')
todolist1.afiseaza_todo_list()
todolist1.afiseaza_detalii_suplimentare('gunoi')
todolist1.afiseaza_todo_list()
todolist2 = ToDoList()
todolist2.adauga_task('factura_telefon','200')
todolist2.afiseaza_todo_list()
todolist2.finalizeaza('factura_telefon')
todolist2.afiseaza_todo_list()
todolist2.afiseaza_detalii_suplimentare('factura_energie')
todolist2.afiseaza_todo_list()
print('---------------------------------------------------------------------------------------------')