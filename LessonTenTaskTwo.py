def summa(i, j, k):
    sum = str(i + j) + k
    return sum


i = int(input('Введите первое число: \n'))
j = int(input('Введите второе число: \n'))
k = input('Введите слово: \n')
print(summa(i, j, k))
