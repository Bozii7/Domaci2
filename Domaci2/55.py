# 55. Napisati program koji za 2 data prirodna broja h i o koji redom predstavljaju broj
# molekula vodonika (H) i kiseonika (O), vraća koliko se najviše molekula vode (H2O)
# može dobiti od datih molekula. Npr., ako je h=4, o=3 odgovor je 2.

h = int(input('Unesi koliko ima molekula h: '))
o = int(input('Unesi koliko ima molekula o: '))

if h // 2 > o:
    print(o)
else:
    print(h // 2)