u = list(input("Введите данные через пробел") .split())
u_list = u
print(u_list)

if len(u_list) % 2 == 0:
    i = 0
    while i < len(u_list):
        e = u_list[i]
        u_list[i] = u_list[i + 1]
        u_list[i + 1] = e
        i += 2
else:
    i = 0
    while i < len(u_list) - 1:
        e = u_list[i]
        u_list[i] = u_list[i + 1]
        u_list[i + 1] = e
        i += 2
print(u_list)