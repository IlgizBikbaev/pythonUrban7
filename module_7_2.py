def custom_write(file_name, strings):
    with open(file_name, 'w', encoding="utf-8") as file:
        strings_positions = {}
        str_count = 0
        str_byte = file.seek(0)
        for str in strings:
            file.write(str + '\n')
            str_count += 1
            key = (str_count, str_byte)
            strings_positions[key] = str
            str_byte = file.tell()
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