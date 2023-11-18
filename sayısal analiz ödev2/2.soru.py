
# ikincisoru
print("<------------------------------------------->")
#  kazım hoca hata payını yapmayın dedigi için aynı fonksiyon soruyu çözdü

a = 1
b = 2

def g(x):
    return x**3+4*x**2-10

def ikiyebol():
    global a,b
    c = (a+b)/2
    if g(c) == 0:
        return c , g(c)
    elif g(a) * g(c) < 0:
        b = c
    else:
        a = c
    return c ,g(c)

print("birinci iterasyon sonucu kök")
print(ikiyebol())
print("ikinci iterasyon sonucu kök")
print(ikiyebol())
print("üçüncü itersayon sonucu kök")
print(ikiyebol())
print("dördüncü iterasyon sonucu kök")
print(ikiyebol())

