def custom_write(file_name: str, strings: str):
    strings_positions = {}
    file = open(file_name, 'w', encoding="utf-8")
    for i in range(len(strings)):
        cursor = file.tell()
        strings_positions[(i+1, cursor)] = strings[i]
        file.write(f"{strings[i]}\n")
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
