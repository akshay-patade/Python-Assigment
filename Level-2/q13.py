class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    inputString = input("Please Enter a string \n")
    inputChar = input("Please enter a character\n")

    x = lambda a, b: print(f"{a[0] == b}\n")

    x(inputString, inputChar)

    if len(inputChar) != 1:
        raise CustomError("Please make sure that you add valid inputs ")

except CustomError as ce:
    print(f"{ce}\n")