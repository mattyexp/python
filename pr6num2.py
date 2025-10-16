N=int(input('Введите длину массива:'))

massiv=[]
for i in range(N):
    massiv.append(int(input('Введите новое целое число:')))

mn=min(massiv)

for i in range(len(massiv)):
    if massiv[i]==mn:
        print(f'Индекс минимального элемента: {i}')

massiv2=[]
massiv3=[]

for i in range(len(massiv)):
    if massiv[i]>0:
        massiv2.append(massiv[i])
    else:
        massiv3.append(massiv[i])

print(f'Первый массив (оригинальный): {massiv}')
print(f'Второй массив (только положительные числа): {massiv2}')
print(f'Третий массив (остальные числа): {massiv3}')