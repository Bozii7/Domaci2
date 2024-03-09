#33. Napisati program koji sabira sve cifre unijetog broja.

a = int(input("Unesi broj: "))
s = 0

while a > 0:
    cif = a % 10
    s = s + cif
    a = a // 10
print(s)