first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i[0]) - len(i[1]) if len(i[0]) > len(i[1]) else len(i[1]) - len(i[0])
                for i in zip(first, second) if len(i[0]) - len(i[1]) or len(i[1]) - len(i[0]) != 0)
second_result = (True if len(first[f]) == len(
    second[s]) else False for f in range(len(first)) for s in range(f, len(second), 3))

print(list(first_result))
print(list(second_result))
