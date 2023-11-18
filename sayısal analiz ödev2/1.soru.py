#1. sonru 2 ye bölme ile kök bulma
a = 2
b = 4
def f(x):
    return x**3 - 2*x**2 - 5

def ikiyebol():
    global a, b, c
    c = (a + b) / 2
    if f(c) == 0:
        return c ,f(c)
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c
    return c ,f(c)

print("birinci iterasyon sonucu kök")
print(ikiyebol())
print("ikinci iterasyon sonucu kök")
print(ikiyebol())
print("üçüncü itersayon sonucu kök")
print(ikiyebol())
print("dördüncü iterasyon sonucu kök")
print(ikiyebol())
