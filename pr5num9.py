text=input('Введите текст:')
slovo=input('Введите слово для поиска:')

text = text.lower()
slovo = slovo.lower()

words=text.split()

count=0
for i in words:
    if i[-1] == '.' or i[-1] == ',':
        current = i[:len(i)-1]
        if current == slovo:
            count+=1
    if i == slovo:
        count+=1

print(f'Слово "{slovo}" встречается в тексте {count} раз(а)')