# 61. Napisati program koji vraća velika slova iz zadatog unijetog teksta kao jedan novi string.
# Ulaz: “Prva recenica. Ovo je druga recenica. Na kraju treca.”
# Izlaz: PON

s = input("Unesi s: ")
s1 = ''

for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z':
        s1 = s1 + s[i]
print(s1)