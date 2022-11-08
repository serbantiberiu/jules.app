'''a. Usor (recomandat)
1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine.
https://www.itfactory.ro/8174437-intro-in-programare/'''

'''b. Usor spre Mediu (obligatoriu)'''

'''1.
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
Afiseaz-o
Inverseaza ordinea folosind slicing si suprascrie aceasta lista
Printeaza varianta actuala (inversata)
Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment. 
'''
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si","do"]
note_muzicale = note_muzicale[::-1]
print("lista inversata", note_muzicale)
note_muzicale.reverse()
print("lista initiala", note_muzicale)

# 2. decate ori apare do

print(f"nota do apare de {note_muzicale.count('do')}")

'''3.
Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gasiti 2 variante sa le uniti intr-o singura lista.
'''
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1 + lista2
print(lista3)
lista1.extend(lista2)
print(lista1)

'''4.
Sortati si afisati lista generata la ex anterior
Stergeti numarul 0 folosind o functie
Afisati iar lista'''
print(lista1)
lista1.sort()
print(f"lista sortata {lista1}")
lista1.remove(0)
print(f"lista dupa stergerea elementului 0 e {lista1}")

'''5.
Folosind un if verificati lista generata la ex3 si afisati
Lista este goala
Lista nu este goala'''
if len(lista1)==0:
    print("lista e goala")
else:
    print("lista nu e goala")


print("6.Folositi o functie care sa stearga lista de la ex3")
# del lista1 - asa sterge lista si din memorie si nu o sa mai mearga ex urmator
lista1.clear()

'''7.
Copy paste la ex 5. Verificati inca o data.
Acum ar trebui sa se afiseze ca lista e goala'''
if len(lista1) == 0:
    print("lista e goala")
else:
    print("lista nu e goala")

'''8.
Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folositi o functie ca sa afisati Elevii (cheile)'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1)
print(dict1.keys())

'''9.
Printati cei 3 elevi si notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o veti lua folosindu-va de cheie'''
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Ana a luat nota {dict1['Dorel']}")

'''10.
Dorel a facut contestatie si a primit 6
Modificati nota lui Dorel in 6
Printati nota dupa modificare'''
dict1["Dorel"] = 6
print(dict1)

'''11.
Gigel se transfera din clasa
Cautati o functie care sa il stearga
Vine un coleg nou. Adaugati Ionica, cu nota 9
Printati noii elevi'''
dict1.pop("Gigel")
print(dict1)
dict1["Ionica"] = 9
print([dict1])

'''12.
Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Adaugati in zilele_sapt ‘luni’
Afisati zile_sapt'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add("luni")
print(zile_sapt)

'''13.
Folositi un if si verificati daca
Weekend este un subset al zilelor din sapt
Weekend nu este un subset al zilelor din sapt'''
if(weekend.issubset(zile_sapt)):
    print("Weekend este un subset al zilelor din sapt")
else:
    print("Weekend nu este un subset al zilelor din sapt")

print("14.Afisati diferentele dintre aceste 2 seturi")
print(zile_sapt.difference(weekend))

print("15.Afisati intersectia elementelor din aceste 2 seturi")
print(weekend.intersection(zile_sapt))

#c. Optionale (may need google)


'''16Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise

Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori
Google search hint
“how to check if item is in list python”
'''

lista_jucatori = ["j1", "j2", "j3", "j4", "j5"]
schimbarie_efectuate = 2
schimbari_maxime = 3
jucator_in = "j7"
jucator_out = "j4"
if jucator_out in lista_jucatori and schimbari_maxime>schimbarie_efectuate:
    print("efectuam schimbarea")
    lista_jucatori.remove(jucator_out)
    lista_jucatori.append(jucator_in)
    schimbarie_efectuate += 1
    print(f'A intrat {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_maxime-schimbarie_efectuate} schimbari')
else:
    if jucator_out in lista_jucatori:
        print('nu mai aveti schimbari')
    else:
        print(f'{jucator_out} nu e in teren')