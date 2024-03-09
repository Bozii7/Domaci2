# 35. Napisati program koji vraća broj cifara u stringu i kreira od njih integer. Primjer: “Hi Mr.
# Rober53. How are you today? Today is 08.10.2019”, štampa 5308102019 i to kao
# integer. Pomoć: da provjerite da li je karakter broj koristiti isdigit metod.

s = input("Unesi string: ")
br = ''
for i in range(len(s)):
    if(s[i] >= '0' and s[i] <= '9'):
        br = br + s[i]
print(int(br))