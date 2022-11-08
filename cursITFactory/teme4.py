import random

# Exercitiul 1 -----------------------------------------------
print('\nE1 - Avand lista "Masini":'
      '\n1. Folositi un FOR ca sa parcurgeti lista si sa afisati "Masina mea preferata este x";'
      '\n2. Faceti acelasi lucru cu un FOR EACH;'
      '\n3. Faceti acelasi lucru cu un WHILE.')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# Cu FOR: ----------------------------------------------
print('\n')
for i in range(len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

# Cu FOR EACH: -----------------------------------------
print('\n')
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# Cu While: --------------------------------------------
print('\n')
i = 0
while i <= len(masini)-1:
    print(f'Masina mea preferata este {masini[i]}')
    i += 1

# Exercitiul 2 -----------------------------------------------
print('----------------------------------------------------------------')
print('\nE2 - In lista de la E1 folositi un FOR pentru a modifica toate elementele cu majuscule'
      '\nexceptand primul si ultimul element.')

print('\n')
for i in range(1, len(masini)-1):
    masini[i] = masini[i].upper()
print(masini)

# Exercitiul 3 -----------------------------------------------
print('----------------------------------------------------------------')
print('\nE3 - In lista de la E1:'
      '\nVine un cumparator care doreste sa cumpere un Mercedes'
      '\nIterati prin ea prin for each'
      '\nDaca masina e mercedes (if)'
      '\n     Printam ‘am gasit masina dorita de dvs’'
      '\n     Iesim din ciclu folosind un cuvant cheie care face acest lucru'
      '\nAltfel'
      '\n     Printam Am gasit masina X. Mai cautam ')

print('\n')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Mercedes':
        print('Am gasit masina dorita!')
        break
    else:
        print(f'Am gasit masina {i}. Mai cautam!')

# Exercitiul 4 -----------------------------------------------
print('----------------------------------------------------------------')
print('\nE4 - In lista de la E1:'
      '\nVine un cumparator bogat dar indecis.'
      '\nIi vom prezenta toate masinile cu exceptia Trabant si Lastun. '
      '\nDaca masina e Trabant sau Lastun'
      '\n     Folositi un cuvant cheie care sa dea skip la ce urmeaza'
      '\nPrintati S-ar putea sa va placa masina x')

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    else:
        print(f'S-ar putea sa va placa masina {masina}')

# Exercitiul 5 -----------------------------------------------
print('----------------------------------------------------------------')
print('\nE5 - Modernizati parcul de masini; '
      '\nCreati o lista goala, masini_vechi in care salvati Lastun si Trabant'
      '\nSuprascrieti-le cu ‘Tesla’ (in lista initiala de masini)'
      '\nPrintati Modele vechi: x Modele noi: x')

masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lastun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# Exercitiul 6 -----------------------------------------------

print('----------------------------------------------------------------')
print('\nE6 - Avand dict "pret_masini", '
      '\nVine un client cu un buget de "X" euro'
      '\nPrezentati doar masinile care se incadreaza in acest buget'
      '\nIterati prin dict.items() si accesati masina si pretul'
      '\nPrintati Pentru un buget de "X" euro puteti alege masina y'
      '\nIterati prin lista')

pret_masini = {"Dacia": 6800, "Lastun": 500, "Opel": 1100, "Audi": 19000, "BMW": 23000}
buget = int(input('\nCe buget aveti pentru masina? :'))
for masina in pret_masini:
    if buget >= pret_masini[masina]:
        print(f'Pentru un buget de {pret_masini[masina]} euro puteti alege masina {masina}')

# Exercitiul 7 -----------------------------------------------
print('----------------------------------------------------------------')
print('\nE7 - Avand lista "numere", iterati prin ea si afisati de cate ori apare 3 fara "count"')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(numere)
total=0
for numar in numere:
    if numar == 3:
        total += 1
print(f'\nNumarul 3 apare de {total} ori.', end="")

# Exercitiul 8 -----------------------------------------------
print('----------------------------------------------------------------')
print('\nE8 - In lista de la E7 calculeaza si afiseaza suma elementelor fara "sum".')

suma = 0
for numar in numere:
    suma += numar
print(f'\nSuma tuturor elementelor este {suma}.')

# Exercitiul 9 -----------------------------------------------

print('----------------------------------------------------------------')
print('\nE9 - Din lista de la E7, afisati cel mai mare numar, fara functia "max".')

nr_max = 0
for numar in numere:
    if numar > nr_max:
        nr_max = numar
print(f'\nCel mai mare numar din lista este {nr_max}.')

# Exercitiul 10 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE10 - In lista de la E7 inlocuieste toate numerele pozitive cu negativul acestora.')

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = numere[i] * -1
print(f'\nNoua lista este: {numere}')

# Exercitiul 11 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE11 - Imparte lista "numere2" in lista de numere pozitive, negative, pare si impare.')

numere2 = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

num_pare = []
num_impare = []
num_poz = []
num_neg = []
for numar in numere2:
    if numar >= 0:
        num_poz.append(numar)
    else:
        num_neg.append(numar)
    if numar % 2 == 0:
        num_pare.append(numar)
    else:
        num_impare.append(numar)
print(f'\nListele sunt:\n Numere pozitive: {num_poz};\n Numere negative: {num_neg};'
      f'\n Numere pare: {num_pare};\n Numere impare: {num_impare}.')

# Exercitiul 12 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE12 - Ordonati crescator lista de la E11 fara functia "sort"')
numere2 = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
aux = 0
for i in range(len(numere2)):
    for j in range(i + 1, len(numere2)):
        if numere2[i] > numere2[j]:
            aux = numere2[i]
            numere2[i] = numere2[j]
            numere2[j] = aux
print(f'\n{numere2}')

# Exercitiul 13 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE13 - Ghicitoare de numar: genereaza un numar de la 1 la 30 si ghiceste-l cu un while.')

numar_random = random.randint(1, 30)
print("numarul de ghicit e ", numar_random)
numar_ghicit=''
while numar_random != numar_ghicit:
    numar_ghicit = int(input('\nGhiceste numarul: '))
    if not numar_ghicit in range(1,31):
        print('Numarul trebuie sa fie intre 1 si 30!')
    elif numar_ghicit < numar_random:
        print('Nr secret e mai mare!')
    elif numar_ghicit > numar_random:
        print('Nr secret e mai mic!')
    else:
        print('Felicitari! Ai ghicit!')


# Exercitiul 14 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE14 - Alegeti un numar de la tastatura si generati o piramida cu acesta precum:'
      '\n1\n22\n333')

n = int(input('\nIntroduceti un numar mai mic decat 10: '))
for x in range(1, n + 1):
    print(x*str(x))

# Exercitiul 15 ----------------------------------------------

print('----------------------------------------------------------------')
print('\nE15 - tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]];'
      '\nCu un "nested for" printati: "Cifra curenta este x"')

tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta e {tastatura_telefon[i][j]}')