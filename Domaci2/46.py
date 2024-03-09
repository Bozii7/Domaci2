# 46. Kreirati program koji nalazi platu zaposlenog koji ima drugo najveće primanje. Npr. ako
# je plate = [540,690, 900] rezultat je 690. Napomena: lista ima bar 2 elementa.

plate = input('Unesite zeljeni niz: ').split()
for i in range(len(plate)):
    plate[i] = eval(plate[i])
najveca = max(plate)
druga_najveca = 9999
for i in plate:
    if najveca - i < druga_najveca and najveca != i:
        druga_najveca = i
print(druga_najveca)