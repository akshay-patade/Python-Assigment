arr = [1, 2, 3, 4, 5]
k = 6

freqArr = {}

#To handle the duplicates
for num in arr:
    if num in freqArr:
        freqArr[num] += 1
    
    else:
        freqArr[num] = 1

arr = list(set(arr))
pairs = 0

i = 0
j = len(arr) - 1

while(i <= j):

    if((arr[i] + arr[j]) == k):

        if arr[i] != arr[j]: # 2,4
            pairs += freqArr[arr[i]] * freqArr[arr[j]]
        else: # 3,3
            pairs += (freqArr[arr[i]] - 1) * (freqArr[i]) // 2
        
        i += 1
        j -= 1

    elif((arr[i] + arr[j]) > k):
        j -= 1
    
    else:
        i += 1

print(f"Pair count: {pairs}")