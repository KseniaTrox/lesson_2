def summary():
    result = 0
    while True:
        print(f"сумма = {result}")
        line_s = input("Введите номер или q для выхода: ").split()  # получаем список строк с цифрами
        for value in line_s:
            if value == "q":
                print(f"сумма = {result}")
                break
            try:
                result += float(values)
            except ValueError:
                print(f" значение {values}")
        else:
            continue
        break
    return f"{result}"


summary()
