from math import sqrt
a=float(input("Введите величену катета 1: "))
b=float(input("Введите величену катета 2: "))
P=a+b+sqrt(a**2+b**2)
S=0.5*a*b
print("Периметр тереугольника=",P)
print("Площадь треугольника=",S)