def logical_or(x, y):
    return x + y - x * y

def logical_xor(x, y):
    return x + y - 2 * x * y

def logical_equ(x, y):
    return 1 - abs(x - y)

def logical_nand(x, y):
    return 1 - x * y

def logical_nor(x, y):
    return 1 - (x + y - x * y)

# A. X OR Y
X = 0  # Tesztérték
Y = 1  # Tesztérték
result_A = logical_or(X, Y)
print(f"A. X OR Y: {result_A}")

# B. X XOR Y
result_B = logical_xor(X, Y)
print(f"B. X XOR Y: {result_B}")

# C. X EQU Y
result_C = logical_equ(X, Y)
print(f"C. X EQU Y: {result_C}")

# D. X NAND Y
result_D = logical_nand(X, Y)
print(f"D. X NAND Y: {result_D}")

# E. X NOR Y
result_E = logical_nor(X, Y)
print(f"E. X NOR Y: {result_E}")

# F. X2*Y2
X2 = 1  # Tesztérték
Y2 = 0  # Tesztérték
result_F = X2 * Y2
print(f"F. X2 * Y2: {result_F}")

# G. 1 - X3
X3 = 0  # Tesztérték
result_G = 1 - X3
print(f"G. 1 - X3: {result_G}")