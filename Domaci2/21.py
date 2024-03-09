from math import sqrt
x = eval(input('Unesite boj \'x\': '))
y = 0
if x <= -7:
    y = -(2*x) + (7/2)
elif -7 < x < 1:
    y = (pow(x, 2)-3*x+5)/(pow(x, 2)+2)
elif 1 <= x <= 8:
    y = sqrt(pow(x, 2)+22*x+2)+sqrt(abs(3/2*x - 4/7))
elif x > 8:
    y = abs(3/pow(x, 2) - 11*x)
print(round(y, 3))