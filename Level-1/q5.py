class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    number = int(input("Please enter a number\n"))
    if(number < 0):
        raise CustomError("Cannot calculate the factorial of negative numbers")

    factorial = 1
    for num in range(1, number + 1):
        factorial *= num
    
    print(f"The factorial of {number} is {factorial}\n")


except ValueError:
    print(f"Please enter only number\n")

except CustomError as ce:
    print(f"{ce}\n")