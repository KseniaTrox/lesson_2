a = int(input("Введите порядковы номер вашего любимого месяца "))
y = {'key_1': 'Весна', 'key_2': 'Лето', 'key_3': 'Осень', 'key_4': 'Зима'}
if a >= 3 and a <= 5:
    print(y.get('key_1'))
if a >= 6 and a <= 8:
    print(y.get('key_2'))
if a >= 9 and a <= 11:
    print(y.get('key_3'))
if a <= 2 or a == 12:
    print(y.get('key_4'))
