# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква в слове {word} : {word[-1]}')


# Вывести количество букв "а" в слове
word = 'Архангельск'
cnt = 0
for symbol in word:
    if symbol.lower() == "а":
        cnt += 1
print(f'Колличество букв "а" в слове {word} : {cnt}')


# Вывести количество гласных букв в слове
word = 'Архангельск'
cnt = 0
vowels = ['а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я']
for symbol in word:
    if symbol.lower() in vowels:
        cnt += 1
print(f'Колличество гласных в слове {word} : {cnt}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Колличество слов в строке "{sentence}"  : {len(sentence.split(" "))}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split(' '):
    print(i[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
median = 0
word_list = sentence.split(' ')
for word in word_list:
    median = median + len(word)
print(f'Средняя длина слова : {median/len(word_list)}')
