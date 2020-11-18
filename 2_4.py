#
# ''' Вариант с циклом'''
# i = 0
# new = []
# for el in my_list:
#     if el > my_list[i - 1]:
#         new.append(el)
#     i += 1
# print(new)
my_list  = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

d = []
gen_list = [d.append(my_list [i + 1]) for i in range(len(my_list ) - 1) if my_list [i] < my_list [i + 1]]
print(d)
