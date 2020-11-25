def my_func(x, y, z):
    iter_obj = [x, y, z]
    iter_obj.remove(min(iter_obj))
    print(sum(iter_obj))


my_func(20,  5, -100)
