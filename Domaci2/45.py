# 45. Kreirati program koji prikazuje koliko ima zaposlenih koji imaju veće plate od prosječne
# plata. Npr. ako su plate = [500, 600, 700] rezultat je 1 jer je samo plata od 700 EUR
# iznad prosječne plate.

plate = input("Unesi plate: ").split()
br = 0
for i in range(len(plate)):
    plate[i] = int(plate[i])
    if(plate[i]) > 650:
        br = br + 1
print(br)