import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x, y, r = sp.symbols('x y r')
eq1 = sp.Eq(2*x**2 + 3*y**2, r)
eq2 = sp.Eq(y, 2*x + 1)
sol = sp.solve([eq1, eq2], [x, y], dict=True)

r_val = 10

x1 = float(sol[0][x].subs(r, r_val))
y1 = float(sol[0][y].subs(r, r_val))
x2 = float(sol[1][x].subs(r, r_val))
y2 = float(sol[1][y].subs(r, r_val))

axis_x = np.linspace(-3, 3, 200)

line_y = 2 * axis_x + 1
y_elips_up = np.sqrt(np.maximum(0, (r_val - 2 * axis_x**2) / 3))
y_elips_bot = -np.sqrt(np.maximum(0, (r_val - 2 * axis_x**2) / 3))

plt.plot(axis_x, line_y, label='y = 2x + 1')
plt.plot(axis_x, y_elips_up, color='blue', label='Ellipse')
plt.plot(axis_x, y_elips_bot, color='blue')

plt.scatter([x1, x2], [y1, y2], color='red', label='Intersections', zorder=5)

plt.xlabel('axis x')
plt.ylabel('axis y')
plt.legend()
plt.grid(True)

plt.savefig('Problem2.pdf')