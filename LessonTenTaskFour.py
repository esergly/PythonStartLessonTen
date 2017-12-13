import random


def poisk(size, num):
    my_list = []
    for i in range(size):
        my_list.append(random.randint(0, size))
    print('Рассматриваемый список:')
    print(my_list)
    result = []
    for i in range(size):
        if my_list[i] == num:
            result.append(i)
    if len(result) == 0:
        print('Искомого числа в списке нет.')
        result = -1
    else:
        print('Искомое число расположено в списке под индексами:')
    return result


size = int(input('Введите длину рассматриваемого списка: \n'))
num = int(input('Введите искомое в списке число: \n'))
print(poisk(size, num))
