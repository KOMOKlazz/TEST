import random

n = int(input('Введите кол дней '))
m = []
count = 0
result = 0
for i in range(0,n):
    random_number = round(random.uniform(-50,50),0)
    m.append(random_number)
    if random_number > 0: 
        count += 1 
        result = count
    else: count = 0
print(n)
print(m)
print(result)