def custom_write(file_name, strings):
    strings_positions = {}
    str_number = 0
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        byte_number = file.tell()
        file.write(f'{i}\n')
        str_number += 1
        key_turple = (str_number, byte_number)
        strings_positions[key_turple] = i
    file.close()
    return strings_positions
    pass



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)