
def text(write):
        if write == 'создать новый файл':
             with open('Lab_3\\user_input.txt', 'w') as file:
                  vvod = input('Введите текст который хотите записать: ')
                  file.write(f"\n{vvod}")
                  return 'Файл создан и текст записан.'
        if write == 'дополнить файл':
             with open('Lab_3\\user_input.txt', 'a') as file:
                  vvod = input('Введите текст для добавления: ')
                  file.write(f"\n{vvod}")
                  return 'Текст добавлен в существующий файл.'
        else:
             print('Ошибка ввода!')

write = input('Вы хотите создать новый файл или дополнить существующий?: ')
print(text(write))