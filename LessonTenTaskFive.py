def words(string):
    temp = list(string)
    count = 0
    for element in temp:
        if element == " ":
            count = count + 1
    count = count + 1
    return count


string = input('Введите строку для подсчёта количества строк: \n')
print(words(string))
