# 66. Data je lista koja se sastoji od cijelih brojeva. Provjeriti da li u listi ima više dvocifrenih ili
# trocifrenih brojeva.

lista = input("Unesi brojeve: ").split()
dvocifreni = 0
trocifreni = 0

for i in lista:
    if len(i) == 3:
        trocifreni = trocifreni + 1
    if len(i) == 2:
        dvocifreni = dvocifreni + 1

if dvocifreni > trocifreni:
    print("Ima vise dvocifrenih")
else:
    print("Ima vise trocifrenih")