def digitize(n):
    n = str(n)
    A = 1
    res = []
    for i in range(0,len(n),A):
        res.append(int(n[i: i + A]))
        
    res.reverse()
    return res