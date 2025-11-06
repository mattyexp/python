# Дана последовательность натуральных чисел (одно число в строке), завершающаяся числом 0.
# Определите значение второго по величине элемента в этой последовательности,
# то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.

def recursion(first_max=0, second_max=0):
    num = int(input())

    if num == 0:
        return second_max
    if num > first_max:
        return recursion(num, first_max)
    elif num > second_max:
        return recursion(first_max, num)
    else:
        return recursion(first_max, second_max)

print("Введите последовательность натуральных чисел (каждое с новой строки)")
print("Чтобы завершить последовательность введите 0")

result = recursion()

print(f"Второе число в последовательности по величине: {result}")