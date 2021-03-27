import sympy

x = sympy.symbols('x')
y = sympy.symbols('y')

expr = x**2+y+1
print(expr)
#x**2+y+1
print(expr.subs(x, 1))
# y+2
print(expr.subs(x, y))
# y**2+y+1
print(expr.subs([(x, 1), (y, 2)]))
# 4

expr = (x+1)**2
print(expr)

expr_ex = sympy.expand(expr)#式の展開
print(expr_ex)

expr_ex = x**2+2*x+1
expr = sympy.factor(expr_ex)#因数分解
print(expr)

print(sympy.factor(x**3-x**2-3*x+3))
print(sympy.factor(x*y+x+y+1))


expr1 = 3*x+5*y-29
expr2 = x+y-7
print(sympy.solve([expr1, expr2]))
#rennrituhouteisiki
#{x: 3, y: 4}

print(sympy.diff(x**3+2*x**2+x))
#bibunn
#3*x**2 + 4*x + 1

expr = x**3+y**2-y
print(sympy.diff(expr, x))
#hennbibunn(x)
#3*x**2

print(sympy.integrate(3*x**2+4*x+1))
#sekibunn
#x**3+2*x**2+x

import sympy
from sympy import diff, integrate, cos, sin, tan

x = sympy.symbols('x')
y = sympy.symbols('y')
z = sympy.symbols('z')

#微分して、(x+1)を足し、積分する関数
#def sikihen(expr, var):
#    expr_1 = integrate((diff(expr)+(x+1)))
#    return expr_1.subs(x, var)

array_f = []
array_k = []
f = x**2+2*x+1
k = diff(f)

for value in range(0, 100):
    array_k.append(k.subs(x, value))
    array_f.append(f.subs(x, value))

print(array_f)
print(array_k)