def factorial(n):
    result = 1
    while n>1:
     result*=n
     n-=1
    return result

def fibonache(n):
    # 0 1 1 2 3 5 8 

    if n == 0:
        return 1
    if n == 1:
        return 2 
    number0 = 0
    number1 = 1
    count = 2
    while n >= number1:
        if n == number1:
            return count
        temp = number1
        number1 += number0
        number0 = temp
        count += 1
    return -1


n = int(input('Введите число '))
print (fibonache(n))