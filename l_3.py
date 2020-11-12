a = int(input("Введите порядковы номер вашего любимого месяца "))
y = ['весна', 'лето', 'осень']
if a >= 3 and a <= 5:
    print(y[0])
if a >= 6 and a <= 8:
    print(y[1])
if a >= 9 and a <= 11:
    print(y[2])
if a <= 2 or a == 12:
    del y
    print('Зима')
