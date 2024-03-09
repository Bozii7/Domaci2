# 32. Napisati program koji za unijete vrijednosti a, b, djelilac vraća sumu i broj elemenata
# djeljivih sa djelilac iz segmenta (a, b) (a i b ne pripadaju intervalu)

a = int(input('Unesite donju granicu: '))
b = int(input('Unesite gornju granicu: '))
djelilac = int(input('Unesite djelioca: '))
suma = 0
brojac = 0
for i in range(a+1, b):
    if i % djelilac == 0:
        suma += i
        brojac += 1
print(suma, brojac)