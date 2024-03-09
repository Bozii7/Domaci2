# 9. Kupili ste zavjesu pravouganog oblika. Provjerite da li će zavjesa prekriti prozor koji je
# takođe pravouganog oblika. Za zavjesu i prozor poznata je gornja lijeva i donja desna
# koordinata.

prozor_gore_lijevo = input('Unesite kordinate gornje lijeve ivice prozora: ').split()
prozor_dolje_desno = input('Unesite kordinate donje desne ivice prozora: ').split()
zavjesa_gore_lijevo = input('Unesite kordinate gornje lijeve ivice zavjese: ').split()
zavjesa_dolje_desno = input('Unesite kordinate donje desne ivice zavjese: ').split()

for i in range(len(prozor_gore_lijevo)):
    prozor_gore_lijevo[i] = eval(prozor_gore_lijevo[i])
    prozor_dolje_desno[i] = eval(prozor_dolje_desno[i])
    zavjesa_gore_lijevo[i] = eval(zavjesa_gore_lijevo[i])
    zavjesa_dolje_desno[i] = eval(zavjesa_dolje_desno[i])

povrsina_prozora = abs(prozor_gore_lijevo[0]-prozor_dolje_desno[0])*abs(prozor_gore_lijevo[1]-prozor_dolje_desno[1])
povrsina_zavjese = abs(zavjesa_gore_lijevo[0]-zavjesa_dolje_desno[0])*abs(zavjesa_gore_lijevo[1]-zavjesa_dolje_desno[1])

if povrsina_prozora > povrsina_zavjese:
    print('Ne pokriva')
else:
    print('Pokriva')