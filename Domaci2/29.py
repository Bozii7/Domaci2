# 29. Napisati program koji provjerava da li je uneseni string binarni broj (ima samo 0 ili 1).

broj = input("Unesi broj: ")

ind = True

for i in range(len(broj)):
    if broj[i] != '0' and broj[i] != '1':
        ind = False
        break

if ind:
    print("Broj je binaran.")
else:
    print("Broj nije binaran")


