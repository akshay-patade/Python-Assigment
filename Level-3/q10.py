numberOfComputers = int(input("Please enter number of Computers\n"))
arrival = input("Please enter arrival and Departure Sequence\n")

currentlyPlaced = set()
notBeenAbleToPlaced = set()

walkAway = 0

for char in arrival:

    if char in notBeenAbleToPlaced: #This will occur when lets say you encountered that character second time and he was not able to sit when he arrived
        pass

    elif char in currentlyPlaced: # Character occured second time and he got the seat
        currentlyPlaced.remove(char)

    
    elif len(currentlyPlaced) < numberOfComputers: # Character occuring for the first time and got a seat
        currentlyPlaced.add(char)
    
    else: #Capacity was full and character did not get the chance to sit
        walkAway += 1
        notBeenAbleToPlaced.add(char)
    
print(walkAway)


