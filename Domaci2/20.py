# 20. Napisati program koji računa zbir parnih cifara ukoliko je broj paran, a ukoliko je neparan
# proizvod neparnih cifara četvorocifrenog broja. Broj n unosi korisnik.

n = int(input("Unesi cetvorocifren broj: "))
if n % 2 == 0:
    cif4 = n % 10
    cif2 = (n // 100) % 10
    sum = cif2 + cif4
    print("Broj je paran", sum)
else:
    cif3 = (n // 10) % 10
    cif1 = n // 1000
    pro = cif1 * cif3
    print("Broj je neparan", pro)
