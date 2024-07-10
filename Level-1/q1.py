try:
    num = int(input("Enter a number\n"))
    if((num % 3) == 0 and (num % 5) == 0):
        print("Consultadd - Python Training\n")
    elif((num % 3) == 0):
        print("Consultadd\n")
    elif((num % 5) == 0):
        print("Python Training\n")

except ValueError:
    print("Please enter only number\n")