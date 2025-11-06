# Из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму
# его цифр и т. д. Через сколько таких действий получится нуль?

def summa(num):
    s = 0
    for i in str(num):
        s += int(i)
    return s

def step(num):
    k = 0
    while num > 0:
        num = num - summa(num)
        k += 1
    return k

num = int(input("Введите целое положительное число: "))
steps = step(num)
print(f"Из числа {num} нужно вычесть сумму его цифр {steps} раз, чтобы получить нуль")