def text(path, method):
    num_lines = {}
    try:
        if method == 1:
            with open(path, 'r') as file: 
                return file.read()
            
        elif method == 2:
            with open(path, 'r') as file: 
                lines = file.readlines()
                for x, i in enumerate(lines, 1):
                    num_lines[f'Строка {x}'] = i.rstrip('\n')
            return num_lines
        
        else:
            return('Ошибка!')
        
    except FileNotFoundError as e:
        return('Ошибка: Файл не найден!\n' + str(e))
    
method = int(input('Выберите способ чтения: \n 1. Полностью\n 2. Построчно\n'))
path = input("Отлично, введите имя файла: ")
print(text(path, method))