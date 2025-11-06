# Упорядочить по возрастанию элементы каждой строки матрицы размером n х m.

def sort(matrix):
    for row in matrix:
        row.sort()

n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

matrix = []
print(f"Введите элементы матрицы {n}x{m} построчно, разделяя числа пробелами:")
for i in range(n):
    addrow = input(f"Введите элементы {i+1}-й строки: ")
    row = [int(s) for s in addrow.split()]
    matrix.append(row)

print("\nИсходная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))

sort(matrix)

print("\nМатрица после сортировки:")
for row in matrix:
    print(" ".join(map(str, row)))
