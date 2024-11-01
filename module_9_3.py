first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = zip(first, second)
first_result = (len(i[0]) - len(i[1]) for i in zp if len(i[0]) - len(i[1]) > 0)
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))
print(list(second_result))
