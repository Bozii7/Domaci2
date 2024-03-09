# 13. Za dva stola kružnog oblika poznat je njihov poluprečnik. Napisati kod kojim se štampa
# obim stola sa većom površinom.

from math import pi

r1 = int(input("Unesi polupercnik prvog stola: "))
r2 = int(input("Unesi polupercnik drugog stola: "))

p1 = r1 * r1 * pi
p2 = r2 * r2 * pi

if p1 > p2:
    print("Veci je prvi sto:", 2 * r1 * pi)
elif p1 < p2:
    print("Veci je drugi sto:", 2 * r2 * pi)
else:
    print("Isti su.")