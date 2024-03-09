# 14. Date su cijene tri proizvoda. Naći par proizvoda čija cijena u zbiru daje najmanju
# vrijednost.

a = int(input("Unesi cijenu prvog proizvoda: "))
b = int(input("Unesi cijenu drugog proizvoda: "))
c = int(input("Unesi cijenu treceg proizvoda: "))

ab = a + b
ac = a + c
bc = b + c

if ab < ac and ab < bc:
    print("A i B:", ab)
elif ac < ab and ac < bc:
    print("A i C:", ac)
elif bc < ab and bc < ac:
    print("B i C:", bc)