try:
    num = int(input("Enter a number\n"))
    sumDigits = 0

    while(num):
        sumDigits += num % 10
        num //= 10
    
    print(f"The sum of the digits is {sumDigits}")

except ValueError:
    print("Please enter only number\n")