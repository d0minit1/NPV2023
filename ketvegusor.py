def ketvegusor_algoritmus(n, k, a):
    b = []

    for i in range(1, k + 1):
        while b and a[i-1] <= a[b[-1]]:
            b.pop()
        b.append(i)

    for i in range(k + 1, n + 1):
        while b and a[i-1] <= a[b[-1]]:
            b.pop()
        b.append(i)
        print(a[b[0] - 1], end=" ")


# A
n_A, k_A, a_A = 3, 3, [1, 2, 3]
print("A. b vektor:", end=" ")
ketvegusor_algoritmus(n_A, k_A, a_A)
print()

# B
n_B, k_B, a_B = 7, 3, [4, 3, 2, 1, 2, 3, 4]
print("B. b vektor:", end=" ")
ketvegusor_algoritmus(n_B, k_B, a_B)
print()

# C
n_C, k_C, a_C = 7, 3, [1, 2, 3, 4, 3, 2, 1]
print("C. b vektor:", end=" ")
ketvegusor_algoritmus(n_C, k_C, a_C)
print()

# D
n_D, k_D, a_D = 7, 3, [3, 5, 2, 1, 7, 2, 8]
print("D. b vektor:", end=" ")
ketvegusor_algoritmus(n_D, k_D, a_D)
print()
