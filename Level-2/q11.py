def character(x):
    return x


strArr = ['Red', 'Blue', 'Black', 'White', 'Pink']

result = []

for word in strArr:
    temp = map(character, word)

    result.append(list(temp))

print(result)

