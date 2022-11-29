# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
x = 'аоиеёэыуюя'
total = 0
for i in range(len(word)):
    if word[i].lower() in x:
        total += 1
print(total)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(sentence.count(' ') + 1)  # 4


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
xr = sentence.split()
xo = [first_letters[0] for first_letters in xr]
print(*xo, sep='\n')


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sum_of_word_lengths = 0 # сумма длин слов
for x in sentence.split():
    word_length = len(x)  # длинна слова
    sum_of_word_lengths += word_length

word_count = len(sentence.split()) # кол-во слов
average = sum_of_word_lengths / word_count
print(int(average))