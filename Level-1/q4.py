class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:
    startBounday = int(input("Enter start bounday\n"))
    endBounday = int(input("Enter end bounday\n"))

    if(startBounday > endBounday):
        raise CustomError("Start boundary should not be greater than the end boundary")

    sumOddNumbes = 0
    sumOddNumbes += sum(num for num in range(startBounday, endBounday + 1, 1) if num % 2 != 0) 

    print(f"The sum of Odd numbers between {startBounday} and {endBounday} is: {sumOddNumbes}\n")


except ValueError:
    print("Please enter only number\n")

except CustomError as ce:
    print(f"{ce}\n")

