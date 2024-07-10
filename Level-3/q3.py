def JtoI():
    with open("q3File.txt", 'r') as file:
        for line in file:
            newLine = line.replace("J", "I")
            print(newLine)

JtoI()

