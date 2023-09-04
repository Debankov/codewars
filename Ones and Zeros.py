def binary_array_to_number(arr):
    binar = ""
    for i in arr:
        binar += str(i)

    return int(binar , base = 2)