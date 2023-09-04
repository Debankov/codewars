def find_next_square(sq):
    nsq = sq ** 0.5
    if int(nsq) == float(nsq):
        nsq = (nsq + 1) ** 2
        return nsq
    else:
        return -1