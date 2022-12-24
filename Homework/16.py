import random

n = int(input('Количество символов: '))
x = int(input('Число, которое надо проверить: '))
A = []
count = 0

for i in range(0, n):
    randomN = round(random.uniform(0, n/2), 0)
    print (randomN)
    if randomN == x:
        count += 1

print(count)