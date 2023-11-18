import math
x1=2
def f(x):
    return 4*math.e**(-1/2*x)-x
def türevf(x):
    return -2*x*math.e**((-3/2)*x)-1

def newton_rapson():
    global x1
    x1 = x1 - f(x1) / türevf(x1)
    return x1 ,f(x1)
print("birinci itersayon sonucu kök")
print(newton_rapson())
print("ikinci itersayon sonucu kök")
print(newton_rapson())
print("üçüncü itersayon sonucu kök")
print(newton_rapson())
print("4.  itersayon sonucu kök")
print(newton_rapson())

