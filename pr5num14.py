stroka=input('Введите строку:')

words=stroka.split()

words1=[]
words2=[]

for i in words:
    i=i.lower()
    if i[-1] == '.' or i[-1] == ',':
        if i[-2]=='я':
            words2.append(i[:len(i)-1])
        if i[0] == 'а':
            words1.append(i[:len(i)-1])
            continue
    if i[0] == 'а':
        words1.append(i)
    if i[-1] == 'я':
        words2.append(i)

print('Слова, начинающиеся на "А":',', '.join(words1))
print('Слова, оканчивающиеся на "Я":',', '.join(words2))

