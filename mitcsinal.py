import math

def valami(a, b):
    x = a
    y = b
    p = 1
    q = 1

    while x != y:
        if x < y:
            r = math.ceil((y - x) / a)
            x += r * a
            p += r
        else:
            r = math.ceil((x - y) / b)
            y += r * b
            q += r

    c = x
    return p, q, c

# A
a_A, b_A = 7, 11
p_A, q_A, c_A = valami(a_A, b_A)
print(f"A. p = {p_A}, q = {q_A}, c = {c_A}")

# B
a_B, b_B = 24, 18
p_B, q_B, c_B = valami(a_B, b_B)
print(f"B. p = {p_B}, q = {q_B}, c = {c_B}")

# C
a_C, b_C = 25, 125
p_C, q_C, c_C = valami(a_C, b_C)
print(f"C. p = {p_C}, q = {q_C}, c = {c_C}")
