# 2. U selu poznatom po svojim jabukama, održava se godišnje takmičenje u berbi jabuka
# između i najbliži pobjedi su Petar i Miloš. Petar tvrdi da je ubrao p jabuka, dok Miloš tvrdi
# da je ubrao m jabuka. Vaš zadatak je da kreirate algoritam koji će provjeriti da li je Petar
# uspio da ubere više jabuka nego Miloš i shodno tome ispiše poruku o pobjedniku.
# Pretpostaviti da ne mogu ubrati isti broj jabuka.

p = int(input("Koliko jabuka je ubrao Pero: "))
m = int(input("Koliko jabuka je ubrao Miki: "))

if p > m:
    print("Petar je ubrao vise jabuka.")
elif p < m:
    print("Milos je ubrao vise jabuka.")
