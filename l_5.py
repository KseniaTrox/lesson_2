x = int(input("Введите число "))
m_list = [7, 5, 2, 3, 2, 1]
i = 0
for n in m_list:
    if x <= n:
        i = i + 1
m_list.insert(i, (x))
print(m_list)
