count = 0
with open("demo.txt", 'r') as file:
    for line in file:
        if len(line.strip().split(" ")) % 2 == 0:
            print(line)