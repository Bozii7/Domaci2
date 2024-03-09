# 58. Napisati program koji od zadatog stringa kreira novi string koji se sastoji bez cifara.
# Primjer: “Hi Mr. Rober53. How are you today? Today is 08.10.2019”), vraća “Hi Mr.
# Rober. How are you today? Today is ..” kao string.
# Pomoć: da provjerite da li je karakter slovo koristiti isalpha metod, a da li je cifre koristite
# isdigit.

s = input("Unesi string: ")
br = ''
for i in range(len(s)):
    if(s[i] >= '0' and s[i] <= '9'):
        br = br + s[i]
print(int(br))