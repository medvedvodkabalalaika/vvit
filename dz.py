import math

def solve(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Нет действительных корней"

a = float(input("Введите первый коэффициент: "))
b = float(input("Введите второй коэффициент: "))
c = float(input("Введите третий коэффициент: "))

result = solve(a, b, c)

print("Корни квадратного уравнения: ", result)