def gcd(x, y):
    if(y == 0):
        return x
    
    return gcd(y, x % y)

try:
    number1 = int(input("Please enter first Number \n"))
    number2 = int(input("Please enter Second Number \n"))

    gcdNumber = gcd(number1, number2)

    lcm = int((number1 * number2) / gcdNumber)

    print(f"The LCM of {number1} and {number2} is {lcm}")


except ValueError:
    print(f"Please enter only Numbers")