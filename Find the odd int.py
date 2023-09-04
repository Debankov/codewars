def find_it(seq):
    for i in range(len(seq)):
        if seq.count(seq[i]) % 2 != 0:
            return seq[i]