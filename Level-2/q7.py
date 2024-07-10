number_list = [7, 2, 5, 1, 9, 3]

number_list.sort()

if len(number_list) & 1:
    print(number_list[len(number_list) // 2])

else:
    median = (number_list[len(number_list) // 2] + number_list[(len(number_list) // 2) - 1]) / 2
    print(median)