import sympy as sp

x, y, r = sp.symbols('x y r')

eq1 = sp.Eq(2*x*x + 3*y*y, r)
eq2 = sp.Eq(2*x + 1, y)
sol = sp.solve([eq1, eq2], [x, y], dict=True)