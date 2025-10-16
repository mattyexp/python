N=int(input('Введите количество целых чисел:'))
result=0
for i in range(N):
    result += int(input('Введите новое число:'))
print('Сумма чисел равна:',result)