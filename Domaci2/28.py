# 28. Napisati program koji provjerava da li se string završava sa target stringom.
# Primjer 1: string:“Abcd”, target: “cd”, štampa se “Da”
# Primjer 2: string: “www.google.com”, target: “me”, štampa se “Ne”

string = input('Unesite string: ')
podstring = input('Unesite podstring: ')
if string.count(podstring) > 0:
    print('Da')
else:
    print('Ne')