input1 = [1, 2, 3, 4, 5]

input1 = list(set(input1)) #Remove Duplicates from input1

input2 = [4, 5, 6, 7, 8]
input2 = list(set(input2)) #Remove Duplicates from input2 

input1.sort()
input2.sort()

result = []

i = 0
j = 0

while i < len(input1) and j < len(input2):
    if(input1[i] == input2[j]):
        result.append(input1[i])
        i += 1
        j += 1
    
    elif(input1[i] > input2[j]):
        j += 1
    
    else:
        i += 1

print(result)