ryad=[0,1]
N=int(input('Введите количество чисел из ряда Фибоначчи: '))
k=0
sum=0


if N<2:
	print('Введите число больше двух')
elif N==2:
	for i in range(len(ryad)):
		sum+=ryad[i]
	print('Сумма чисел ряда:',sum)
elif N>2:
	i=0
	while k!=N-2:
		new=ryad[i]+ryad[i+1]
		ryad.append(new)
		i+=1
		k+=1
	for i in range(len(ryad)):
		sum+=ryad[i]
	print('Сумма чисел ряда:',sum)