n = [1, 2, 3, 4, 5]
k = int(input("Введите количество пропусков"))
result = []
for i in range(0, k):
    n.insert(0, n[-1])
    n.pop(-1)
print(n)