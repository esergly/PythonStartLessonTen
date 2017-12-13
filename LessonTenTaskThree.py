# Взял тоже самое решение, что написал для задачи из четвёртой лекции, но оформил через функцию.

def rectangle(vysota, shirina):
    temp = vysota
    while vysota > 0:
        if vysota == temp or vysota == 1:
            print("*" * shirina)
        else:
            print('*' + ' ' * (shirina - 2) + '*')
        vysota = vysota - 1


vysota = int(input('Введите высоту прямоугольника: '))
shirina = int(input('Введите ширину прямоугольника: '))
rectangle(vysota, shirina)
