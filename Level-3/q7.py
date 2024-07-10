studentNames = ["Sam", "Alice", "Mona"]
studentSubjects = ["Commerce", "Science", "Computer"]

mapping = {}

for i in range(0, len(studentNames)):
    mapping[studentNames[i]] = studentSubjects[i]


print(mapping)
