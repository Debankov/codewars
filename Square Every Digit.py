def square_digits(num):
    nums = [int(i) for i in str(num)]
    res = ""
    for j in nums:
        count = int(j)**2
        res = res + str(count)
    return int(res)