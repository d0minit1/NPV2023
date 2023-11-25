def lindenmayer_rendszer(kezdo_allapot, szabalyok, iteraciok):
    aktualis_allapot = kezdo_allapot

    for _ in range(iteraciok):
        uj_allapot = ""
        for karakter in aktualis_allapot:
            if karakter in szabalyok:
                uj_allapot += szabalyok[karakter]
            else:
                uj_allapot += karakter
        aktualis_allapot = uj_allapot

    return aktualis_allapot


# A
kezdo_allapot_A = "A"
szabalyok_A = {"A": "AB", "B": "A"}
eredmeny_A = lindenmayer_rendszer(kezdo_allapot_A, szabalyok_A, 4)
print("A. Eredmény:", eredmeny_A)

# B
kezdo_allapot_B = "A"
szabalyok_B = {"A": "B[A]", "B": "BB"}
eredmeny_B = lindenmayer_rendszer(kezdo_allapot_B, szabalyok_B, 4)
print("B. Eredmény:", eredmeny_B)

# C
kezdo_allapot_C = "A"
szabalyok_C = {"A": "AB", "B": "BA"}
eredmeny_C = lindenmayer_rendszer(kezdo_allapot_C, szabalyok_C, 4)
print("C. Eredmény:", eredmeny_C)

# D
kezdo_allapot_D = "F"
szabalyok_D = {"F": "F+G", "G": "FG"}
eredmeny_D = lindenmayer_rendszer(kezdo_allapot_D, szabalyok_D, 4)
print("D. Eredmény:", eredmeny_D)

# E
kezdo_allapot_E = "PQ"
szabalyok_E = {"P": "Q-Q", "Q": "PR"}
eredmeny_E = lindenmayer_rendszer(kezdo_allapot_E, szabalyok_E, 4)
print("E. Eredmény:", eredmeny_E)
