import math


def lines(my_list):
    if my_list[2] - my_list[1] == my_list[1] - my_list[0]:
        return my_list[len(my_list) - 1] + my_list[2] - my_list[1]
    if my_list[2] / my_list[1] == my_list[1]:
        return round(my_list[len(my_list) - 1] * my_list[2] / my_list[1])
    if (my_list[1] - my_list[0]) ** 2 == my_list[2]:
        return round((math.sqrt(my_list[len(my_list) - 1]) + 1) ** 2)
    if ((my_list[1]) ** (1 / 3)) == (my_list[0] + 1):
        return round(((my_list[len(my_list) - 1] ** (1 / 3)) + 1) ** 3)


line = input('Введите строку последовательности: \n')
my_list = []
i = 0
while i < len(line):
    line_int = ''
    a = line[i]
    while '0' <= a <= '9':
        line_int += a
        i += 1
        if i < len(line):
            a = line[i]
        else:
            break
    i += 1
    if line_int != '':
        my_list.append(int(line_int))

print(lines(my_list))
