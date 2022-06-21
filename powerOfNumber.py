# How to calculate power of a number using recursion

def power(base, exp):
    assert 0 < exp == int(exp), "Error, exponent must be positive integer."
    if exp == 0:
        return 0
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

print(power(3, 3))