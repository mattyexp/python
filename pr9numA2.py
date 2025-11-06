# Дано натуральные числа a,b Вычислить остаток от деления a на b

def recursion(a, b):
    if a < b:
        return a
    else:
        return recursion(a - b, b)

a = int(input('Введите натуральное число a (делимое): '))
b = int(input('Введите натуральное число b (делитель, b > 0): '))

if b<=0:
    print('b должно быть больше нуля')
else:
    result = recursion(a, b)
    print(f"Остаток от деления {a} на {b} равен: {result}")