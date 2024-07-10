Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
freqList = {}

for number in Input_list:
    if number in freqList:
        freqList[number] += 1
    else:
        freqList[number] = 1

print(freqList)

