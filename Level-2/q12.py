username = input("Please enter your username\n")
tries = 0

while(tries < 3):
    password = input("Please enter your password\n")
    retypePassword = input("Please again enter your password\n")

    if(password == retypePassword):
        print(f"Welcome, {username}")
        exit()
    
    tries += 1
    print(f"Password does not match with retype Password. Please try again\n")

print("System locked!!! Please contact administrator")