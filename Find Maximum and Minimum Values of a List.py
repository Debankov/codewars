def minimum(arr):
    temp = arr[0]
    for i in range(len(arr)):
        if arr[i] <= temp:
            temp = arr[i]
    return temp
        

def maximum(arr):
    temp = arr[0]
    for i in range(len(arr)):
        if arr[i] >= temp:
            temp = arr[i]
    return temp