print("Введите число в промежутке от -5 до -1 или от 3 до 8")

x = float(input())

if x >= -5 and x <= -1 or x >= 3 and x < 8:
    print("Число попало в промежуток") 
else:
    print("Число вне промежутка")
