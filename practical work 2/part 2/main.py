import math
print("Введите число t")

t = float(input())

a = t + 4
b = t
c = 3 * t - 10

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)

elif D == 0:
    x = -b / (2 * a)
    print("x = ", x)
else:
    print("Нет решений уравнения")

