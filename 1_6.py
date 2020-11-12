n_list = []
p_list = []
s_list = []
a_list = []
i = 0
a = int(input("Введите кол-во товарных позиций "))
while i <= a - 1:
    if i <= a - 1:
        n = input("Введите название")
        p = input("Введите цену  ")
        s = int(input("Введите количество "))
        n_list.append(n)
        p_list.append(p)
        s_list.append(s)
        n_dict = {"название": n_list}
        p_dict = {"цена": p_list}
        s_dict = {"количество": s_list}
        b = tuple([i + 1, {"название": n, "цена": p, "количество ед": s }])
        a_list.append(b)
        i = i + 1
else:
   for z in a_list:
    print(z)
print(n_dict)
print(p_dict)
print(s_dict)

