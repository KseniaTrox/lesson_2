def sum_num():
    r = 0
    while True:
        my_list = input("Введите числа через пробел, для выхода введите x: ").split()
        for num in my_list:
            if num == 'x':
                return r
            else:
                try:
                    r += int(num)
                except ValueError:
                    print("Для выхода из программы введите  x ")
        print(f"Сумма  введенных чисел = {r}")


print(sum_num())
