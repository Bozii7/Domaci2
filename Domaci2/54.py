# 54. Dat je string sastavljen od karaktera 0 i 1. Karakter 0 predstavlja slobodno polje, a 1
# predstavlja zauzeto polje. Vaš zadatak je da za zadatu poziciju u stringu provjerite da li
# su susjedna polja slobodna (lijevo i desno). Napomena: za prvo polje gledate same
# desno polje, za poslednje polje samo lijevo polje, a za ostala i lijevo i desno polje. Npr.
# ako je string 01010, a zadata pozicija 2 (indeksiranje kreće od nule), treba štampati 0 jer
# nema slobodnih polja.

tekst = input('Unesite zeljeni tekst: ')
pozicija = int(input('Unesite zeljenu poziciju: '))

if pozicija == 0:
    if tekst[pozicija+1] == '0':
        print('1')
    else:
        print('0')
elif pozicija == len(tekst)-1:
    if tekst[pozicija-1] == '0':
        print('1')
    else:
        print('0')
else:
    br = 0
    if tekst[pozicija-1] == '0':
        br += 1
    if tekst[pozicija+1] == '0':
        br += 1
    print(br)