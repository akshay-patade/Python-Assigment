class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

"""Assuming that for every subject , a student can get 100 marks"""
try:
    physics = int(input("Enter Physics Marks\n"))
    if(physics > 100):
        raise CustomError("Physics Marks cannot be Greater than 100")

    chemisty = int(input("Enter Chemistry Marks\n"))
    if(chemisty > 100):
        raise CustomError("Chemistry Marks cannot be Greater than 100")

    biology = int(input("Enter biology Marks\n"))
    if(biology > 100):
        raise CustomError("Biology Marks cannot be Greater than 100")

    mathematics = int(input("Enter Mathematics Marks\n"))
    if(mathematics > 100):
        raise CustomError("Mathematics Marks cannot be Greater than 100")

    computer = int(input("Enter Computer Marks\n"))
    if(mathematics > 100):
        raise CustomError("Computer Marks cannot be Greater than 100")


    percentage = round(((physics + chemisty + biology + mathematics + computer)) / 5)

    if percentage >= 90:
        print("Grade A")
    elif percentage >= 80:
        print("Grade B")
    elif percentage >= 70:
        print("Grade C")
    elif percentage >= 60:
        print("Grade D")
    elif percentage >= 50:
        print("Grade E")
    else:
        print("Grade F") 
        
except ValueError:
    print("Please enter only number as an input\n")

except CustomError as ce:
    print(f"{ce}\n")