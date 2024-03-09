# 1. U tajanstvenom svijetu postoji portal koji se otvara samo kada mu se date paran broj.
# Kao mladi čarobnjak na svom prvom zadatku, dobio si čarobni štapić koji može
# generisati brojeve. Vaš zadatak je da kreirate algoritam koji će provjeriti da li je broj koji
# je čarobni štapić generisao paran. Ako jeste, algoritam treba da ispiše: "Portal se
# otvara!" Ako nije, algoritam treba da ispiše: "Portal ostaje zatvoren."

a = int(input("Unesi broj: "))
if a % 2 == 0:
    print("Portal se otvara!")
else:
    print("Portal ostaje zatvoren")