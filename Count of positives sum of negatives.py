def count_positives_sum_negatives(arr):
    pos = 0
    neg = 0
    for i in arr:
        if i > 0:
            pos += 1
        else:
            neg += i
            
    res = []
    if len(arr) == 0:
        return res
    else:
        res = [pos, neg]
        return res