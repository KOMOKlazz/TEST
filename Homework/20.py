w = str(input('Введите слово: '))
points = 0

one = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r']
two = ['d', 'g']
three = ['b', 'c', 'm', 'p']
four = ['f', 'h', 'v', 'w', 'y']
five = ['k']
eight = ['j', 'x']
ten = ['q', 'z']

for i in w:
    if i in one:
        points += 1
    if i in two:
        points += 2
    if i in three:
        points += 3
    if i in four:
        points += 4
    if i in five:
        points += 5
    if i in eight:
        points += 8
    if i in ten:
        points += 10

print('Ты набрал', points, 'очков')