import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

# Define las variables simbólicas
x, y = symbols('x y')

# Define la función
f = x**2 + y**2

# Calcula las derivadas parciales
df_dx = diff(f, x)
df_dy = diff(f, y)

# # Convierte las derivadas a funciones numéricas
# df_dx_num = lambdify((x, y), df_dx, 'numpy')
# df_dy_num = lambdify((x, y), df_dy, 'numpy')

# Convierte la función simbólica a una función numérica
f_num = lambdify((x, y), f, 'numpy')

# Rango de valores para x e y
x_vals = np.linspace(-10, 10, 20)
y_vals = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x_vals, y_vals)

# # Calcula los gradientes
# grad_x = df_dx_num(X, Y)
# grad_y = df_dy_num(X, Y)

# Calcula los valores de la función
Z = f_num(X, Y)

# # Graficar el campo de gradientes
# plt.figure(figsize=(8, 6))
# plt.quiver(X, Y, grad_x, grad_y, color='blue', angles='xy', scale_units='xy', scale=1)
# plt.title("Campo de gradientes de $f(x, y) = x^2 + y^2$")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid()
# plt.show()

# Crear la figura y el gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

# Configurar etiquetas y título
ax.set_title("Gráfico 3D de $f(x, y) = x^2 + y^2$")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")

plt.show()


