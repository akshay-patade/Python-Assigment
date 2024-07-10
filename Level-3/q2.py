count = 0
with open("demo.txt", 'r') as file:
    for line in file:
        count += 1

print(count)