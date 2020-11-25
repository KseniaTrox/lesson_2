def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y не может быть равен 0"


print(my_func(int(input("Введите целое число x = ")), int(input("Введите y = "))))
#
