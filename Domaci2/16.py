# 16. Napisati program kojim se provjerava da li se tačka nalazi unutar pravouganika. Za
# pravougaonik su date koordinate gornjeg lijevog i donjeg desnog tjemena.

gornja_lijeva = input('Unesite kordinate gornjeg lijevog tjemena: ').split()
donja_desna = input('Unesite kordinate donjeg desnog tjemena: ').split()
tjeme_korsnika = input('Unesite kordinate caseg tjemena: ').split()

for i in range(2):
    gornja_lijeva[i] = eval(gornja_lijeva[i])
    donja_desna[i] = eval(donja_desna[i])
    tjeme_korsnika[i] = eval(tjeme_korsnika[i])

if gornja_lijeva[0] <= tjeme_korsnika[0] <= donja_desna[0] and gornja_lijeva[1] >= tjeme_korsnika[1] >= donja_desna[1]:
    print('Vase tjeme pripada pravougaoniku')
else:
    print('Vase tjeme nepripada pravougaoniku')