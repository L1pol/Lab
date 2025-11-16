def text(write):
    try:
        if write == 'целиком':
            with open('Lab_3\exampte.txt', 'r') as file: # изминена буква в названии файла
                return file.read()
        elif write == 'построчно':
            with open('Lab_3\example.txt', 'r') as file: # правильное название файла
                return file.readlines()
        else:
            return('Ошибка!')
    except FileNotFoundError:
        return( 'Ошибка: Файл не найден!')
    
write = input('Какой формат чтения вы хотите выбрать?\nчтение целиком или построчно?: ')
print(text(write))