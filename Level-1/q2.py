userInput = input("Please enter a string\n")
alphabets = 0
numbers = 0

for x in userInput:
    if(x.isdigit()):
        numbers += 1
    
    elif(x.isalpha()):
        alphabets += 1
    
print(f"Alphabets: {alphabets} & Number : {numbers}")