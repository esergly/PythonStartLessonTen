result = 0
buffer = 0

for i in range(100, 1000, 1):
    for j in range(100, 1000, 1):
        buffer = j * i
        if buffer > result:
            result = buffer
        temp = list(str(result))
        if len(temp) == 5:
            if temp[0] == temp[4] and temp[1] == temp[3]:
                print('Число ' + str(result) + ' является палиндроном и являет собой произведением чисел ' + str(
                    j) + ' and ' + str(i))
        if len(temp) == 6:
            if temp[0] == temp[5] and temp[1] == temp[4] and temp[2] == temp[3]:
                print('Число ' + str(result) + ' является палиндроном и являет собой произведением чисел ' + str(
                    j) + ' and ' + str(i))
