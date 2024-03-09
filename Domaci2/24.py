# 24. Ako tekst ima više od 30 karaktera skratiti ga tako da ostane tačno 30 karaktera, a na
# kraj skraćenog teksta dodati …

s = input("Unesi tekst: ")

if len(s) > 30:
    novi_tekst = s[:30]
    novi_tekst += '...'
    print(novi_tekst)
