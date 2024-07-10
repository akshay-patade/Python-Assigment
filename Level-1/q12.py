try:
    num = int(input("Enter a number\n"))
    revNumber = 0
    temp = num

    while(temp):
        revNumber = revNumber * 10 + temp % 10
        temp //= 10
    
    print(f"The reverse of {num} is {revNumber}")

except ValueError:
    print("Please enter only number\n")