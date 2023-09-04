def get_grade(s1, s2, s3):
    sa = (s1+s2+s3)/3
    if  sa >= 90 and sa <= 100:
        return "A"
    elif sa >= 80 and sa <90:
        return "B"
    elif sa >= 70 and sa <80:
        return "C"
    elif sa >= 60 and sa <70:
        return "D"
    elif sa >= 0 and sa <60:
        return "F"