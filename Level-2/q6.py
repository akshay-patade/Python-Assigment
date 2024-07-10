def isPower2(num):
    if num <= 1:
        return True

    elif num % 2 == 1:
        return False
    
    return isPower2(num // 2)

try:
    num = int(input("Enter a number\n"))
    result = isPower2(num)
    
    if result:
        print(f"{num} is a power of 2\n")
    
    else:
        print(f"{num} is not a power of 2\n")
    

except ValueError:
    print("Please enter only number\n")
