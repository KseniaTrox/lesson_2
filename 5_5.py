f = open('num.txt', 'w', encoding='utf-8')
s = input('введите чиcла через пробел:')
j = []
f.write(s)
f = open('num_1.txt', 'r', encoding='utf-8')
cont = f.readline()
d = cont.split(' ')
for f in d:
    y = int(f)
    j.append(y)
    sum = 0
    for i in j:
        sum = sum + i
print(sum)
