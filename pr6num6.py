massiv=[]
for i in range(10):
    N=int(input('Введите новое число:'))
    massiv.append(N)

mx=max(massiv)

overcount=0
undercount=0
for i in massiv:
    if i<mx:
        undercount+=1
    if i>mx:
        overcount+=1
    
print(f'Количество элементов меньших максимального: {undercount} и количество больших максимального элемента: {overcount}')

sum=0
for i in massiv:
    if i>5:
        sum+=i
print(f'Сумма чисел из массива >5 равна: {sum}')