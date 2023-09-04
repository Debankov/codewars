def sum_array(arr):
    if arr == None:
        return 0 
    
    for i in range(0,len(arr)):
        if arr[i] == None:
            return 0

    if len(arr) <= 1:
        return 0

    res = 0
    for i in range(0,len(arr)):
        res += arr[i]
        
    res = res - min(arr) - max(arr)    
    return res