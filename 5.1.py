# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.Об
# окончании ввода данных свидетельствует пустая строка.
f = open('grumbler.txt', 'w', encoding='utf-8')
while True:
    s = input('введите строку:')
    if s == '': break  # пустая строка
    f.write(s + '\n')
f.close()
f = open('grumbler.txt', 'r')
content = f.read()
print(content)
f.close()
