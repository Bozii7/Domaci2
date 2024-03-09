# 10. Vaš zadatak je da napišete program kojim provjerate da li je strelica pogodila pikado
# tablu. Za pikado tablu je poznat je njegov poluprečnik i koordinate centra, a za strelice
# koordinate cilja.

from math import sqrt
pikado_centar = {
    'x': 2,
    'y': 3,
    'poluprecnik': 2,
}

x = float(input('Unesite x kordinatu: '))
y = float(input('Unesite y kordinatu: '))
rastojanje = sqrt(pow(x-pikado_centar['x'], 2)+pow(y-pikado_centar['y'], 2))

if rastojanje > pikado_centar['poluprecnik']:
    print('Strelica nije pogodila pikado.')
else:
    print('Strelica je pogodila pikado.')