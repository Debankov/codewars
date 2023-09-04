def DNA_strand(dna):
    nucleotides = list(dna.lower());
    complementary = ""
    for base in nucleotides:
        if base == "a":
            complementary += "t";
        if base == "t":
            complementary += "a";
        if base == "c":
            complementary += "g";
        if base == "g":
            complementary += "c";
    return complementary.upper();