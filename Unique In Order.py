def unique_in_order(sequence):
    res = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            res.append(sequence[i])
    return res