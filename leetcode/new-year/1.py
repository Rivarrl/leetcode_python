def q():
    x = 'def q():\n    x = {}\n    return x.format(repr(x))'
    return x.format(repr(x))

a = q()
print(a)
