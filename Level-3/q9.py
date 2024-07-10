inputString = input("Please input the string\n")

i = 0

result = ""

while(i < len(inputString)):

    j = i
    while(j < len(inputString) and inputString[i] == inputString[j]):
        j += 1
    
    result += inputString[i] + str(j - i)
    i = j

print(result)
    
