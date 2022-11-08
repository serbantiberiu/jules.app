# Exercitiul 1 -----------------------------------------------

print('\nE1 - Functie care sa calculeze si sa returneze suma a 2 numere.')

def sum(x, y):
    return x+y

# Exercitiul 2 -----------------------------------------------

print('----------------------------------------------------------------')
print('\nE2 - Functie care sa returneze TRUE daca un numar este par, FALSE pt impar.')

def paritate(x):
    if x % 2 == 0:
        return True
    else:
        return False

# Exercitiul 3 -----------------------------------------------
print('----------------------------------------------------------------')
print('\nE3 - Functie care returneaza numarul total de caractere din numele tau complet.'
      '\n(nume, prenume, nume_mijlociu)')

# Am exclus spatiile si liniutele din nume la numararea caracterelor.
# Exemplu: "Teligradeanu Bertoni-Mihai" este citit "TeligradeanuBertoniMihai"
def nr_char(nume):
    nume = nume.replace(" ", "")
    nume = nume.replace("-", "")
    return len(nume)

# Exercitiul 4 -----------------------------------------------

print('----------------------------------------------------------------')
print('\nE4 - Functie care returneaza aria dreptunghiului.')

def aria_d(lungime, latime):
    return lungime*latime

# Exercitiul 5 -----------------------------------------------

print('----------------------------------------------------------------')
print('\nE5 - Functie care returneaza aria cercului.')

PI = 3.141592653589793  # Ca sa nu import toata libraria :)


def aria_c(raza):
    return PI*raza**2

# Exercitiul 6 -----------------------------------------------

print('----------------------------------------------------------------')
print('\nE6 - Functie care returneaza True daca un caracter x se gaseste intr-un'
      '\nstring dat; Fasle daca nu.')

STRING = 'A4593458jnauuvnrlijllweoewmBNWQZPU'

def cauta(caracter):
    return caracter in STRING

# Exercitiul 7 -----------------------------------------------

print('----------------------------------------------------------------')
print('\nE7 - Functie fara return, primeste un string si printeaza pe ecran:'
      '\n* Nr de caractere lower case este x;'
      '\n* Nr de caractere upper case exte y.')

def count(text):
    lower = 0
    upper = 0
    for i in range(len(text)):
        if text[i].islower():
            lower += 1
        elif text[i].isupper():
            upper += 1
    print(f'Nr. de caractere lower case este {lower}')
    print(f'Nr. de caractere upper case este {upper}')

count('AlalaLLaal')

# Exercitiul 8 -----------------------------------------------

print('----------------------------------------------------------------')
print('\nE8 - Functie care primeste o LISTA de numere si returneaza o LISTA '
      '\ndoar cu numerele pozitive.')

def lista_poz(lista_numere):
    lista_numere_poz = []
    for numar in lista_numere:
        if numar >= 0:
            lista_numere_poz.append(numar)
    return lista_numere_poz

# Exercitiul 9 -----------------------------------------------

print('----------------------------------------------------------------')
print('\nE9 - Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA'
      '\n* Primul numar x este mai mare decat al doilea nr y'
      '\n* Al doilea nr y este mai mare decat primul nr x'
      '\n* Numerele sunt egale. ')


def comparator1(x, y):
    if x == y:
        print('Numerele sunt egale!')
    elif x > y:
        print(f'{x} este mai mare decat {y}!')
    else:
        print(f'{y} este mai mare decat {x}!')


# Exercitiul 10 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE10 - Functie care primeste un numar si un set de numere.'
      '\n*Printeaza ‘am adaugat numarul nou in set’ + returneaza True;'
      '\n*Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False')
set_numere = {1, 9, 4, 7, 2}

def set_nr(nr, set_numere):
    if nr in set_numere:
        print("Printeaza ‘nu am adaugat numarul in set. Acesta exista deja")
        return False
    else:
        set_numere.add(nr)
        print('Am adaugat numarul nou in set!')
        return True
# Exercitiul 11 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE11 - Functie care primeste o luna din an si returneaza cate zile are acea luna.')
luna_31 = ["Ianuarie",  "Martie", "Mai",
        "Iulie", "August", "Octombrie", "Decembrie"]
luna_30 =["Aprilie", "Iunie", "Septembrie", "Noiembrie"]
def zile_luna(luna, an=0):
    if luna in luna_31:
        return 31
    elif luna in luna_30:
        return 30
    else:
        if an %4 == 0 and an % 100 != 100:
            return 29
        elif an%400 == 0:
            return 29
        else:
            return 28

# Exercitiul 12 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE12 - Functie calculator care sa returneze 4 valori: Suma, diferenta, inmultirea, impartirea a 2 numere.'
      '\nIn final vei putea face:'
      '\na, b, c, d = calculator(10, 2)'
      '\nprint("Suma: ", a)'
      '\nprint("Diferenta: ", b)'
      '\nprint("Inmultirea: ", c)'
      '\nprint("Impartirea: ", d)')

def calculator(a,b):
    return a+b, a-b, a*b, a/b

a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

#alta metoda
print("suna este:", calculator(5,4)[0])


# Exercitiul 13 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE13 - Functie care primeste o lista de cifre (adica doar 0-9) si returneaza un DICT '
      '\ncare ne spune de cate ori apare fiecare cifra')

list = [1, 3, 1, 5, 9, 7, 7, 5, 5, 8, 2, 1, 0]


def nr(lista):
    dic ={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i in lista:
        dic[i] = lista.count(i)
    return dic

# Exercitiul 14 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE14 - Functie care primeste 3 numere; Returneaza valoarea maxima dintre ele.')

def maxim(a,b,c):
    return max(a,b,c)

# Exercitiul 15 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE15 - Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar.')

def suma(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

# Exercitiul 16 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE16 - Functie care primesete 2 liste de numere (numerele pot fi dublate); Returnati numerele comune')

lista1 = [1, 2, 23, 4, 7, 9, 4, 2]
lista2 = [4, 5, 7, 34, 23, 5, 6, 8]

def numere_comune():
    return set(lista1).intersection(lista2)

# Exercitiul 17 ----------------------------------------------
print('----------------------------------------------------------------')
print('\nE17 - Functie care sa aplice o reducere de pret.Daca produsul costa 100 lei si aplicam reducere de 10%'
      'Pretul va fi 90.Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida')

def reducere(pret, reducere):
    if reducere < 0 or reducere>100:
        print(f"Reducere nu se poate efectua. {reducere} trebuie sa fie intre 0 si 100")
    print(f"Noul pret va fi {pret-((reducere/100)*pret)}")

# Exercitiul 18 ----------------------------------------------
print('----------------------------------------------------------------')
print('\nE18 - Functie care sa afiseze data si ora curenta din ro(bonus: afisati si data si ora curenta din China)')
from datetime import datetime
import pytz
def data_ora_curenta(region):
    tz = pytz.timezone(region)  # china timezone
    time = datetime.now(tz)
    print(time)


data_ora_curenta('Asia/Shanghai')
data_ora_curenta('Europe/Bucharest')

# Exercitiul 19 ----------------------------------------------
print('----------------------------------------------------------------')
print('\nE19 - Functie care sa afiseze cate zile mai sunt pana la ziua ta / '
      'sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)')

from datetime import datetime
import time


def data_ora_curenta(zi, luna):
    ## dd/mm/yyyy format
    current_day = time.strftime("%d/%m/%Y")

    #
    if luna > int(time.strftime("%m")):
        my_birthday = str(zi) + "/" + str(luna) + "/" + time.strftime("%Y")
    elif luna < int(time.strftime("%m")):
        my_birthday = str(zi) + "/" + str(luna) + "/" + str(int(time.strftime("%Y")) + 1)
    else:
        if zi >= int(time.strftime("%d")):
            my_birthday = str(zi) + "/" + str(luna) + "/" + time.strftime("%Y")
        else:
            my_birthday = str(zi) + "/" + str(luna) + "/" + str(int(time.strftime("%Y")) + 1)

    # dates in string format

    # convert string to date object
    d1 = datetime.strptime(my_birthday, "%d/%m/%Y")
    d2 = datetime.strptime(current_day, "%d/%m/%Y")

    # difference between dates in timedelta
    days_number = d1 - d2
    if days_number.days == 0:
        print('Azi e ziua ta!!La multi ani!!!')
    else:
        print(f'Difference is {days_number.days} days')