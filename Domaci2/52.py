# 52. Napisati program koji na osnovu varijabli a, pre, sub i num dodaje prefiks pre, i sufiks suf
# stringu a num puta i vraća novi prošireni string.
# Input 1: a = ‘test’, pre = ‘pr’, suf = ‘su’, num = 2;
# Output 1: ‘prprtestsusu’

tekst = input('Unesite zeljeni tekst: ')
pre = input('Unesite prefiks: ')
suf = input('Unesite sufinks: ')
num = int(input('Unesite koliko puta zelite da se prefiks i sufiks ponavljaju: '))

pre *= num
suf *= num
print(pre+tekst+suf)