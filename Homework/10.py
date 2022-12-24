import random

n = int(input('Введите кол монеток '))
m = []
result = 0

for i in range(0,n):
    random_num = round(random.randint(0,1))
    m.append(random_num)
    if random_num == 0 : result += 1

print (m)
print (result)
