# 60. Napisati program koji na osnovu dvije varijable start i end koji predstavljaju početak i kraj
# segmenta [start, end] (uključujući start i end) kvadrira sve elemente iz tog segmenta koji
# su djeljivi sa 3 ali ne sa 6, a onda ih sumira. Štampati sumu.

start = int(input("Unesi pocetak: "))
end = int(input("Unesi kraj: "))
s = 0

for i in range(start, end + 1):
    if i % 2 == 0 and i % 4 != 0:
        i = i*i
        s += i
print(s)