# 48. Napisati program koji račun X**n koristeći petlju (bez ugrađenog Python operatora za
# stepenovanje)

broj = int(input('Unesite zeljeni broj koji zelite stepenovati: '))
stepen = int(input('Unesite zeljeni stepen: '))
resenje = 1
while stepen > 0:
    resenje *= broj
    stepen -= 1
print(resenje)