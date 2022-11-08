'''Set
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