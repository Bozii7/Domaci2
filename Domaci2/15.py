# 15. Napisati kod koji za datu godinu određuje da li je prestupna i štampa odgovarajuću
# poruku.

godina = int(input("Unesi godinu: "))

if godina % 4 == 0:
    print("Godina je prestupna.")
else:
    print("Godina nije prestupna")