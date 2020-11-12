your_t = list(input("Введите несколько слов через пробел ").split())
for i, el in enumerate(your_t, 1):
    if len(el) > 10:
        el = el[:10]
    print(f"{i}. {el}")
