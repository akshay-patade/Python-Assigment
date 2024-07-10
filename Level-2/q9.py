try:
    lst = []

    n = int(input("Please enter number of elements in the list\n"))

    print("Please enter values\n")
    for i in range(0, n):
        ele = int(input())
        # adding the element
        lst.append(ele) 
    
    print(lst[7]) #Here we are trying to access element at 8th pos but we have total of only 5 elements

except ValueError:
    print(f"Please enter only integer values in the string\n")

except IndexError:
    print(f"Index out of bounds\n")


