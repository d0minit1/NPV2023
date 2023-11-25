def automata_jelsorozat(automata, jelsorozat):
    allapot = 1  # Az automata kezdeti állapota
    allapotok = [allapot]  # Az állapotokat tároló lista

    for jel in jelsorozat:
        allapot = automata[allapot][jel]  # Az állapotváltozás az aktuális jel hatására
        allapotok.append(allapot)

    return allapotok

# Az automata átmenetek leírása
automata_atmenetek = {
    1: {'A': 1, 'B': 3},
    2: {'A': 2, 'B': 1},
    3: {'A': 3, 'B': 2}
}

# A. BBAABB jelsorozat
jelsorozat_A = "BBAABB"
eredmeny_A = automata_jelsorozat(automata_atmenetek, jelsorozat_A)
print(f"A. Az állapotok a BBAABB jelsorozat hatására: {eredmeny_A}")

# B. AABAAB jelsorozat
jelsorozat_B = "AABAAB"
eredmeny_B = automata_jelsorozat(automata_atmenetek, jelsorozat_B)
print(f"B. Az állapotok az AABAAB jelsorozat hatására: {eredmeny_B}")

# C. BABBABA jelsorozat
jelsorozat_C = "BABBABA"
eredmeny_C = automata_jelsorozat(automata_atmenetek, jelsorozat_C)
print(f"C. Az állapotok a BABBABA jelsorozat hatására: {eredmeny_C}")

# D. BAABABAB jelsorozat
jelsorozat_D = "BAABABAB"
eredmeny_D = automata_jelsorozat(automata_atmenetek, jelsorozat_D)
print(f"D. Az állapotok a BAABABAB jelsorozat hatására: {eredmeny_D}")

# E. Milyen jelsorozat szükséges ahhoz, hogy az automata a végén 3-as állapotban legyen?
# A válasz: BABA
jelsorozat_E = "BABA"
eredmeny_E = automata_jelsorozat(automata_atmenetek, jelsorozat_E)
print(f"E. Az állapotok a BABA jelsorozat hatására: {eredmeny_E}")