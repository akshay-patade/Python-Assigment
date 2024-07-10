count = 0
inputString = input("Please enter the string \n")

firstName = ""
lastName = ""
id = ""

for i  in range(len(inputString)):

    if ((i + 1) < len(inputString) and  inputString[i] == '0' and  inputString[i + 1] != '0'):
        count += 1
    
    elif(inputString[i] == '0'):
        continue

    elif count == 0:
        firstName += inputString[i]

    elif count == 1:
        lastName += inputString[i]

    else:
        id += inputString[i]

finalDict = {
    "first_name" : firstName,
    "last_name" : lastName,
    "id" : id
}

print(finalDict)