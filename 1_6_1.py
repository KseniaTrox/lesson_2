goods = []
while input("Хотите добавить товар? Введите да / нет:: ") == 'да':
    number = int(input("Введите номер продукта: "))
    features = {}
    while input("Хотите добавить параметры продукта? Введите да / нет: ") == 'да':
        feature_key = input("Введите функциональный продукт: ")
        feature_value = input("Enter feature value product : ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
#goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)


while i <= a - 1:
    if i <= a -1:
        n = input("Введите название")
        p = input("Введите цену ")
        s = input("Введите количество ")
        n_list.append(n)
        p_list.append(p)
        s_list.append(s)
        n_dict = {"название": n_list}
        p_dict = {"цена": p_list}
        s_dict = {"количество": s_list}
        b = tuple([i + 1, {"название": n, "цена": p, "количество": s}])
        a_list.append(b)
        i = i + 1
else:
    for z in a_list:
        print(z)
print(n_dict)
print(p_dict)
print(s_dict)