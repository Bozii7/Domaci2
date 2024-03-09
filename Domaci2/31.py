# 31. Napisati program sa dva ulaza (korisnik unosi) start i end koji predstavljaju početak i kraj
# segmenta [start, end] (uključujući start i end), a koja kvadrira sve elemente iz tog
# segmenta koji su djeljivi sa 2 ali ne sa 4, a onda ih sumira. Štampati sumu.

start = int(input("Unesi pocetak: "))
end = int(input("Unesi kraj: "))
s = 0

for i in range(start, end + 1):
    if i % 2 == 0 and i % 4 != 0:
        i = i*i
        s += i
print(s)