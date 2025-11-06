# Даны 3 различных массива целых чисел. В каждом массиве найти
# произведение элементов и среднеарифметическое значение.

def processing(array):
    # произведение элементов
    result = 1
    for num in array:
        result = result * num
    print(f"Произведение элементов: {result}")

    # среднеарифметическое значение
    total = sum(array)
    answer = total / len(array)
    print(f"Среднеарифметическое значение: {round(answer,2)}")

first = input("Введите элементы первого массива целых чисел через пробел: ")
first_array = [int(s) for s in first.split()]

second = input("Введите элементы второго массива целых чисел через пробел: ")
second_array = [int(s) for s in second.split()]

third = input("Введите элементы третьего массива целых чисел через пробел: ")
third_array = [int(s) for s in third.split()]

print("\n--- Обработка первого массива ---\n")
processing(first_array)
print("\n--- Обработка второго массива ---\n")
processing(second_array)
print("\n--- Обработка третьего массива ---\n")
processing(third_array)