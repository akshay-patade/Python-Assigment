class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    number = int(input("Please enter a positive  number \n"))
    sumDivisors = 0
    if(number <= 0):
        raise CustomError("Please enter only positive numbers")

    sumDivisors = sum(num for num in range(1, number) if number % num == 0)

    if(sumDivisors == number):
        print("YES")
    
    else:
        print("NO")

except ValueError:
    print(f"Please enter only postive numbers \n")

except CustomError as ce:
    print(f"{ce}\n")