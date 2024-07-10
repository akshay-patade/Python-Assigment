numberOfPiles = int(input("Please enter number of piles\n"))
startValue = numberOfPiles

result = []

for i in range(numberOfPiles):
    result.append(startValue)
    startValue += 2

print(result)
