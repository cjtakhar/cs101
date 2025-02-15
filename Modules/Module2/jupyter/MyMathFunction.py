def exponent(base, exp):
    result = 1

    for i in range(0, exp):
        result *= base

    return result