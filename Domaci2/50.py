# 50. Napisati program koji iz zadatog stringa izdvaja samo samoglasnike i vraća taj novi
# string.

s = input("Unesi string: ")
s1 = ''

for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        s1 = s1 + s[i]
print(s1)

