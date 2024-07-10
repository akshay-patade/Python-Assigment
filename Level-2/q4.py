arr = [1, 2, 3, 4, 5]
D = 2

D = D % len(arr)


newArr = arr[len(arr) - D : len(arr)] + arr[0 : len(arr) - D]

print(newArr)