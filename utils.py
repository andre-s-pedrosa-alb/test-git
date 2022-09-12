
def sum(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    assert b != 0
    return a / b

def power(a, b):
    if b < 0:
        return 1/power(a, -b)
    if b == 0:
        return 1
    if b == 1:
        return a
    return a**b
