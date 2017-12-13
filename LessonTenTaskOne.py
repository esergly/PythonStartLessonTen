def max_of_list(my_list):
    my_list.sort()
    return my_list[len(my_list) - 1]


my_list = [5, 7, 8, 1, 2, 9, 5, 5, 3]
print(str(max_of_list(my_list)))
