# 5. Napisati program kojim se proverava da li se može napraviti bašta u obliku trougla sa
# datim dužinama stranica.

a = int(input('Unesi stranicu a: '))
b = int(input('Unesi stranicu b: '))
c = int(input('Unesi stranicu c: '))

if a + b > c and a + c > b and b + c > a:
    print('Moze biti u obliku trougla.')
else:
    print('Ne moze biti u obliku trougla.')