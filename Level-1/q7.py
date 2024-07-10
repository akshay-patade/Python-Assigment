string1 = input("Enter first string\n")
string2 = input("Enter second string\n")

result = True

if(len(string1) != len(string2)):
    result = False

if(result):

    freqString1 = {}
    freqString2 = {}

    for char in string1:
        if char in freqString1:
            freqString1[char] += 1
        else:
            freqString1[char] = 1
    
    for char in string2:
        if char in freqString2:
            freqString2[char] += 1
        else:
            freqString2[char] = 1
    
    for char in string2:

        if(not(char in freqString1) or freqString1[char] != freqString2[char]):
            result = False
            break

print(result)
